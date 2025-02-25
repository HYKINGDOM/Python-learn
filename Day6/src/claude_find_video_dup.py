import os
import hashlib
import cv2
import numpy as np
import argparse
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import logging
from tqdm import tqdm
import time
import shutil
from collections import defaultdict
import json
import psutil
import torch
import gc

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("video_deduplication.log"),
        logging.StreamHandler()
    ]
)

class ResourceMonitor:
    """资源监控类，用于监控CPU、内存和GPU使用情况"""
    def __init__(self):
        self.use_cuda = torch.cuda.is_available()
        self.total_memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)  # GB
        self.cpu_count = psutil.cpu_count(logical=False)

        if self.use_cuda:
            self.gpu_name = torch.cuda.get_device_name(0)
            self.gpu_memory = torch.cuda.get_device_properties(0).total_memory / (1024 * 1024 * 1024)  # GB

        logging.info(f"系统信息: CPU: {self.cpu_count}核, 内存: {self.total_memory:.2f}GB")
        if self.use_cuda:
            logging.info(f"GPU: {self.gpu_name}, 显存: {self.gpu_memory:.2f}GB")

    def get_memory_usage(self):
        """获取当前内存使用情况"""
        memory = psutil.virtual_memory()
        used_percent = memory.percent
        used_gb = memory.used / (1024 * 1024 * 1024)
        return used_percent, used_gb

    def get_gpu_usage(self):
        """获取GPU使用情况"""
        if not self.use_cuda:
            return 0, 0

        used_memory = torch.cuda.memory_allocated(0) / (1024 * 1024 * 1024)  # GB
        used_percent = (used_memory / self.gpu_memory) * 100
        return used_percent, used_memory

    def get_cpu_usage(self):
        """获取CPU使用情况"""
        return psutil.cpu_percent(interval=0.1)

    def check_resources(self, mem_threshold=85, cpu_threshold=90, gpu_threshold=85):
        """检查资源使用是否超过阈值"""
        mem_percent, mem_used = self.get_memory_usage()
        cpu_percent = self.get_cpu_usage()

        if self.use_cuda:
            gpu_percent, gpu_used = self.get_gpu_usage()
            is_overloaded = (mem_percent > mem_threshold or
                             cpu_percent > cpu_threshold or
                             gpu_percent > gpu_threshold)

            if is_overloaded:
                logging.warning(f"资源使用过高! 内存: {mem_percent:.1f}% ({mem_used:.2f}GB), "
                                f"CPU: {cpu_percent:.1f}%, GPU: {gpu_percent:.1f}% ({gpu_used:.2f}GB)")
        else:
            is_overloaded = (mem_percent > mem_threshold or cpu_percent > cpu_threshold)

            if is_overloaded:
                logging.warning(f"资源使用过高! 内存: {mem_percent:.1f}% ({mem_used:.2f}GB), "
                                f"CPU: {cpu_percent:.1f}%")

        return is_overloaded

    def recommend_workers(self, default=4):
        """根据系统资源推荐工作进程数量"""
        # 考虑CPU核心数，保留一个核心给系统
        cpu_based = max(1, self.cpu_count - 1)

        # 考虑内存情况，每个worker估计使用1-2GB内存
        mem_info = psutil.virtual_memory()
        available_mem_gb = mem_info.available / (1024 * 1024 * 1024)
        mem_based = max(1, int(available_mem_gb / 2))

        # 取较小值以确保不会过载
        recommended = min(cpu_based, mem_based, default)
        logging.info(f"推荐的工作进程数: {recommended} (基于CPU核心数: {cpu_based}, 可用内存: {mem_based})")

        return recommended

class VideoDeduplicator:
    def __init__(self, root_dir, output_dir=None, sample_rate=10, frame_count=5,
                 similarity_threshold=0.95, use_size_filter=True, max_workers=None,
                 use_gpu=True, batch_size=32, resource_check_interval=30):
        """
        初始化视频重复检测器

        参数:
            root_dir (str): 要扫描的根目录
            output_dir (str): 重复文件移动到的输出目录
            sample_rate (int): 每隔多少秒采样一帧
            frame_count (int): 每个视频采样的帧数
            similarity_threshold (float): 相似度阈值，超过此值认为是重复视频
            use_size_filter (bool): 是否使用文件大小预过滤
            max_workers (int): 最大并行进程数，None表示自动确定
            use_gpu (bool): 是否使用GPU加速特征提取
            batch_size (int): GPU处理时的批量大小
            resource_check_interval (int): 资源检查间隔(秒)
        """
        self.root_dir = os.path.abspath(root_dir)
        self.output_dir = output_dir
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.sample_rate = sample_rate
        self.frame_count = frame_count
        self.similarity_threshold = similarity_threshold
        self.use_size_filter = use_size_filter

        # 资源监控与管理
        self.resource_monitor = ResourceMonitor()
        self.max_workers = max_workers if max_workers is not None else self.resource_monitor.recommend_workers()
        self.resource_check_interval = resource_check_interval
        self.last_resource_check = time.time()

        # GPU相关设置
        self.use_gpu = use_gpu and torch.cuda.is_available()
        self.batch_size = batch_size
        if self.use_gpu:
            logging.info(f"将使用GPU加速特征提取")
            self.device = torch.device("cuda:0")
        else:
            self.device = torch.device("cpu")
            logging.info(f"将使用CPU进行特征提取")

        self.video_extensions = {
            '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
            '.m4v', '.mpg', '.mpeg', '.3gp', '.ts', '.mts', '.m2ts',
            '.vob', '.ogv', '.rm', '.rmvb', '.asf', '.divx'
        }
        self.size_groups = defaultdict(list)
        self.signatures = {}
        self.duplicates = defaultdict(list)
        self.total_videos = 0
        self.processed_videos = 0
        self.results_file = "duplicate_videos_results.json"

        # 优化的参数
        self.chunk_size = 4 * 1024 * 1024  # 4MB，针对SSD优化
        self.thread_chunk_size = 100  # 线程批处理大小

    def is_video_file(self, file_path):
        """检查文件是否为视频文件"""
        return os.path.splitext(file_path)[1].lower() in self.video_extensions

    def get_file_size_category(self, size):
        """获取文件大小类别，用于预分组"""
        if size < 1024 * 1024:  # 小于1MB
            return "small_" + str(size // (1024 * 50))  # 50KB为一组
        elif size < 10 * 1024 * 1024:  # 小于10MB
            return "medium_" + str(size // (1024 * 1024))  # 1MB为一组
        elif size < 100 * 1024 * 1024:  # 小于100MB
            return "large_" + str(size // (5 * 1024 * 1024))  # 5MB为一组
        else:
            return "xlarge_" + str(size // (50 * 1024 * 1024))  # 50MB为一组

    def scan_videos(self):
        """扫描目录下的所有视频文件并按大小分组"""
        logging.info(f"开始扫描目录: {self.root_dir}")

        video_files = []
        total_size = 0

        # 使用os.walk快速扫描所有文件
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if self.is_video_file(file_path):
                        file_size = os.path.getsize(file_path)
                        video_files.append((file_path, file_size))
                        total_size += file_size
                except (OSError, IOError) as e:
                    logging.error(f"无法访问文件 {file_path}: {e}")

        self.total_videos = len(video_files)
        total_size_gb = total_size / (1024 * 1024 * 1024)
        logging.info(f"找到 {self.total_videos} 个视频文件，总大小: {total_size_gb:.2f} GB")

        # 根据系统内存调整预分组逻辑
        if self.total_videos > 100000:  # 超大规模文件集
            logging.info("检测到超大规模文件集，启用更精细的分组策略")
            # 更精细的分组以减少每组的比较量
            self.use_size_filter = True

        if self.use_size_filter:
            for file_path, file_size in video_files:
                size_category = self.get_file_size_category(file_size)
                self.size_groups[size_category].append((file_path, file_size))

            # 统计分组信息
            group_sizes = {k: len(v) for k, v in self.size_groups.items()}
            largest_groups = sorted(group_sizes.items(), key=lambda x: x[1], reverse=True)[:5]
            logging.info(f"文件大小分组: {len(self.size_groups)} 组")
            logging.info(f"最大的5个组: {largest_groups}")
        else:
            # 如果不使用大小过滤，按照合理的批次分组以控制内存使用
            batch_size = min(5000, max(100, len(video_files) // 20))  # 动态确定批次大小
            for i in range(0, len(video_files), batch_size):
                batch = video_files[i:i+batch_size]
                batch_id = f"batch_{i//batch_size}"
                self.size_groups[batch_id] = batch

            logging.info(f"未使用大小过滤，创建了 {len(self.size_groups)} 个批次组")

        return self.total_videos

    def compute_video_signature_gpu(self, video_paths):
        """使用GPU批量计算视频特征签名"""
        results = {}

        for video_path in video_paths:
            try:
                # 视频预处理仍需在CPU上进行
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    logging.warning(f"无法打开视频: {video_path}")
                    continue

                # 获取视频基本信息
                fps = cap.get(cv2.CAP_PROP_FPS)
                if fps <= 0:
                    fps = 25  # 默认FPS
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                duration = total_frames / fps

                if duration <= 0 or total_frames <= 0:
                    logging.warning(f"视频 {video_path} 无效的时长或帧数")
                    cap.release()
                    continue

                # 确定采样间隔
                if duration <= self.sample_rate * self.frame_count:
                    # 视频太短，平均采样
                    interval = max(1, total_frames // (self.frame_count + 1))
                    sample_frames = [i * interval for i in range(1, self.frame_count + 1)]
                else:
                    # 按指定采样率采样
                    frames_to_skip = int(fps * self.sample_rate)
                    start_frame = frames_to_skip
                    sample_frames = [start_frame + i * frames_to_skip for i in range(self.frame_count)]
                    sample_frames = [min(f, total_frames - 1) for f in sample_frames if f < total_frames]

                if not sample_frames:
                    logging.warning(f"视频 {video_path} 无法提取足够的帧")
                    cap.release()
                    continue

                # 提取帧
                frames = []
                for frame_idx in sample_frames:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
                    ret, frame = cap.read()
                    if not ret:
                        continue

                    # 调整大小并转为灰度图
                    frame = cv2.resize(frame, (32, 32))
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # 计算梯度特征
                    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
                    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)

                    # 特征向量
                    frame_feature = np.concatenate([
                        gray.flatten() / 255.0,
                        np.abs(grad_x).flatten() / np.max(np.abs(grad_x)) if np.max(np.abs(grad_x)) > 0 else np.zeros_like(grad_x.flatten()),
                        np.abs(grad_y).flatten() / np.max(np.abs(grad_y)) if np.max(np.abs(grad_y)) > 0 else np.zeros_like(grad_y.flatten())
                    ])

                    frames.append(frame_feature)

                cap.release()

                if not frames:
                    continue

                # 将帧特征转换为张量并计算平均值
                if self.use_gpu:
                    with torch.no_grad():
                        frames_tensor = torch.tensor(frames, device=self.device, dtype=torch.float32)
                        final_feature = torch.mean(frames_tensor, dim=0)
                        # 归一化
                        norm = torch.norm(final_feature)
                        if norm > 0:
                            final_feature = final_feature / norm
                        # 转回CPU和NumPy
                        final_feature = final_feature.cpu().numpy()
                else:
                    # CPU计算
                    final_feature = np.mean(frames, axis=0)
                    # 归一化
                    norm = np.linalg.norm(final_feature)
                    if norm > 0:
                        final_feature = final_feature / norm

                results[video_path] = final_feature

            except Exception as e:
                logging.error(f"处理视频 {video_path} 时出错: {e}")
                continue

        return results

    def compute_video_signature(self, video_path):
        """计算单个视频特征签名"""
        results = self.compute_video_signature_gpu([video_path])
        return results.get(video_path)

    def compute_partial_hash(self, file_path):
        """计算文件的部分哈希，仅读取文件的头部、中部和尾部"""
        try:
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                return None

            hasher = hashlib.md5()

            # 根据文件大小调整读取策略
            if file_size < 5 * 1024 * 1024:  # 小于5MB的文件
                # 小文件直接读取开头部分
                with open(file_path, 'rb') as f:
                    hasher.update(f.read(min(file_size, self.chunk_size)))
            else:
                with open(file_path, 'rb') as f:
                    # 读取开头部分
                    head_data = f.read(self.chunk_size)
                    hasher.update(head_data)

                    if file_size > self.chunk_size * 2:
                        # 读取中间部分
                        f.seek(file_size // 2 - self.chunk_size // 2)
                        middle_data = f.read(self.chunk_size)
                        hasher.update(middle_data)

                    if file_size > self.chunk_size:
                        # 读取结尾部分
                        f.seek(max(0, file_size - self.chunk_size))
                        tail_data = f.read(self.chunk_size)
                        hasher.update(tail_data)

            return hasher.hexdigest()
        except Exception as e:
            logging.error(f"计算文件 {file_path} 哈希时出错: {e}")
            return None

    def compute_hashes_batch(self, files_batch):
        """并行计算一批文件的哈希"""
        results = {}
        for file_path, _ in files_batch:
            hash_value = self.compute_partial_hash(file_path)
            if hash_value:
                results[file_path] = hash_value
        return results

    def process_video_group(self, video_group):
        """处理一组视频文件"""
        if self.resource_monitor.check_resources():
            # 资源使用过高，减少处理量
            if len(video_group) > 100:
                logging.warning(f"资源使用率高，将大组 ({len(video_group)} 个文件) 分成更小的批次处理")
                mid = len(video_group) // 2
                results1 = self.process_video_group(video_group[:mid])
                # 强制垃圾回收
                gc.collect()
                if self.use_gpu:
                    torch.cuda.empty_cache()
                results2 = self.process_video_group(video_group[mid:])
                return results1 + results2

        results = []

        # 使用ThreadPoolExecutor并行计算哈希
        hash_groups = defaultdict(list)
        with ThreadPoolExecutor(max_workers=min(16, self.max_workers * 2)) as executor:
            futures = []

            # 将视频按批次提交给线程池
            for i in range(0, len(video_group), self.thread_chunk_size):
                batch = video_group[i:i+self.thread_chunk_size]
                futures.append(executor.submit(self.compute_hashes_batch, batch))

            # 收集哈希结果
            for future in futures:
                batch_hashes = future.result()
                for file_path, hash_value in batch_hashes.items():
                    file_size = next(size for path, size in video_group if path == file_path)
                    hash_groups[hash_value].append((file_path, file_size))

        # 对每个哈希组内的视频进行内容特征比较
        for hash_value, video_files in hash_groups.items():
            # 如果哈希组只有一个文件，肯定不是重复的
            if len(video_files) == 1:
                continue

            # 先判断是否是完全相同的文件（哈希相同、大小相同）
            size_groups = defaultdict(list)
            for video_path, file_size in video_files:
                size_groups[file_size].append(video_path)

            # 处理完全相同的文件
            for size, files in size_groups.items():
                if len(files) > 1:
                    primary = files[0]
                    for duplicate in files[1:]:
                        results.append((primary, duplicate, 1.0, "exact_hash_match"))

            # 对于哈希相同但大小不同的文件，计算内容特征进行比较
            if len(size_groups) > 1:
                all_videos = []
                for size_group_files in size_groups.values():
                    all_videos.extend(size_group_files)

                # 分批计算特征以控制内存使用
                features = {}
                for i in range(0, len(all_videos), self.batch_size):
                    batch = all_videos[i:i+self.batch_size]

                    # 检查资源使用情况
                    if time.time() - self.last_resource_check > self.resource_check_interval:
                        self.last_resource_check = time.time()
                        if self.resource_monitor.check_resources():
                            # 资源紧张，减小批量大小
                            self.batch_size = max(1, self.batch_size // 2)
                            logging.info(f"资源使用较高，减小批处理大小至 {self.batch_size}")

                            # 清理一些内存
                            gc.collect()
                            if self.use_gpu:
                                torch.cuda.empty_cache()

                    # 批量计算特征
                    batch_features = self.compute_video_signature_gpu(batch)
                    features.update(batch_features)

                # 两两比较计算相似度
                for i, video1 in enumerate(all_videos):
                    if video1 not in features:
                        continue
                    for j in range(i + 1, len(all_videos)):
                        video2 = all_videos[j]
                        if video2 not in features:
                            continue

                        # 使用GPU计算相似度
                        if self.use_gpu:
                            with torch.no_grad():
                                v1_feature = torch.tensor(features[video1], device=self.device)
                                v2_feature = torch.tensor(features[video2], device=self.device)
                                similarity = torch.dot(v1_feature, v2_feature).item()
                        else:
                            # CPU计算相似度
                            similarity = np.dot(features[video1], features[video2])

                        if similarity >= self.similarity_threshold:
                            # 保留大文件作为主文件
                            v1_size = os.path.getsize(video1)
                            v2_size = os.path.getsize(video2)
                            if v1_size >= v2_size:
                                results.append((video1, video2, float(similarity), "content_match"))
                            else:
                                results.append((video2, video1, float(similarity), "content_match"))

                # 清理缓存
                del features
                gc.collect()
                if self.use_gpu:
                    torch.cuda.empty_cache()

        return results

    def find_duplicates(self):
        """查找重复视频"""
        if not self.size_groups:
            self.scan_videos()

        logging.info("开始查找重复视频...")
        all_results = []

        # 动态调整工作进程数
        current_workers = self.max_workers

        # 预估每个组的大小，优先处理小组
        group_sizes = [(category, len(videos)) for category, videos in self.size_groups.items()]
        group_sizes.sort(key=lambda x: x[1])  # 按组大小排序

        with tqdm(total=len(self.size_groups), desc="处理视频组") as pbar:
            with ProcessPoolExecutor(max_workers=current_workers) as executor:
                futures = {}
                active_futures = 0
                max_active = current_workers * 2  # 控制同时活跃的任务数

                # 提交和处理任务
                for size_category, size in group_sizes:
                    videos = self.size_groups[size_category]

                    if len(videos) <= 1:  # 跳过只有一个视频的组
                        pbar.update(1)
                        continue

                    # 检查资源使用情况
                    if time.time() - self.last_resource_check > self.resource_check_interval:
                        self.last_resource_check = time.time()
                        if self.resource_monitor.check_resources():
                            # 资源紧张，减少并行度
                            current_workers = max(1, current_workers - 1)
                            max_active = current_workers * 2
                            logging.info(f"资源使用较高，减少工作进程数至 {current_workers}")

                            # 等待一些任务完成以释放资源
                            while active_futures >= max_active and futures:
                                done, _ = ProcessPoolExecutor.wait(
                                    futures.keys(),
                                    return_when="FIRST_COMPLETED"
                                )
                                for future in done:
                                    size_cat = futures.pop(future)
                                    active_futures -= 1
                                    try:
                                        results = future.result()
                                        all_results.extend(results)
                                        logging.info(f"完成组 {size_cat}，找到 {len(results)} 对重复")
                                    except Exception as e:
                                        logging.error(f"处理组 {size_cat} 时出错: {e}")
                                    pbar.update(1)

                    # 控制并发任务数量
                    while active_futures >= max_active:
                        done, _ = ProcessPoolExecutor.wait(
                            futures.keys(),
                            return_when="FIRST_COMPLETED"
                        )
                        for future in done:
                            size_cat = futures.pop(future)
                            active_futures -= 1
                            try:
                                results = future.result()
                                all_results.extend(results)
                                logging.info(f"完成组 {size_cat}，找到 {len(results)} 对重复")
                            except Exception as e:
                                logging.error(f"处理组 {size_cat} 时出错: {e}")
                            pbar.update(1)

                    # 提交新任务
                    future = executor.submit(self.process_video_group, videos)
                    futures[future] = size_category
                    active_futures += 1

                # 等待所有剩余任务完成
                for future in futures:
                    size_category = futures[future]
                    try:
                        results = future.result()
                        all_results.extend(results)
                        logging.info(f"完成组 {size_category}，找到 {len(results)} 对重复")
                    except Exception as e:
                        logging.error(f"处理组 {size_category} 时出错: {e}")
                    pbar.update(1)

        # 整理结果
        for primary, duplicate, similarity, match_type in all_results:
            self.duplicates[primary].append({
                "path": duplicate,
                "similarity": similarity,
                "match_type": match_type
            })

        # 保存结果
        self.save_results()

        return self.duplicates

    def save_results(self):
        """保存重复检测结果到JSON文件"""
        results = {}
        for primary, duplicates in self.duplicates.items():
            results[primary] = duplicates

        with open(self.results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        logging.info(f"结果已保存到 {self.results_file}")

    def remove_duplicates(self, move_instead=True):
        """删除或移动重复文件"""
        if not self.duplicates:
            logging.warning("没有找到重复文件")
            return

        total_removed = 0
        total_size_saved = 0

        # 批量处理，避免单次处理太多文件
        duplicates_list = []
        for primary, duplicates in self.duplicates.items():
            for dup_info in duplicates:
                duplicates_list.append((primary, dup_info))

        # 每批处理的文件数
        batch_size = 100
        total_batches = len(duplicates_list) // batch_size + (1 if len(duplicates_list) % batch_size else 0)

        with tqdm(total=len(duplicates_list), desc="处理重复文件") as pbar:
            for i in range(total_batches):
                start = i * batch_size
                end = min(start + batch_size, len(duplicates_list))
                batch = duplicates_list[start:end]

                for primary, dup_info in batch:
                    dup_path = dup_info["path"]
                    try:
                        file_size = os.path.getsize(dup_path)
                        if move_instead:
                            if self.output_dir:
                                shutil.move(dup_path, os.path.join(self.output_dir, os.path.basename(dup_path)))
                                logging.info(f"移动重复文件: {dup_path} -> {self.output_dir}")
                            else:
                                logging.warning("未指定输出目录，跳过移动操作")
                        else:
                            os.remove(dup_path)
                            logging.info(f"删除重复文件: {dup_path}")

                        total_removed += 1
                        total_size_saved += file_size
                    except OSError as e:
                        logging.error(f"处理文件 {dup_path} 时出错: {e}")

                    pbar.update(1)

        logging.info(f"共移除或删除 {total_removed} 个重复文件，节省空间 {total_size_saved / (1024 * 1024 * 1024):.2f} GB")
