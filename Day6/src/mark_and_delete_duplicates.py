import hashlib
import os
from collections import defaultdict
from multiprocessing import Pool, cpu_count


def calculate_file_hash(file_path, hash_algorithm='md5', chunk_size=8192, sample_size=1024 * 1024):
    """
    计算文件的哈希值（优化版：只计算文件的部分内容）
    :param file_path: 文件路径
    :param hash_algorithm: 哈希算法（默认MD5）
    :param chunk_size: 每次读取的块大小
    :param sample_size: 采样大小（默认1MB）
    :return: 文件的哈希值
    """
    hash_func = hashlib.new(hash_algorithm)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        # 读取文件头部
        hash_func.update(f.read(min(sample_size, file_size)))
        # 如果文件较大，读取文件中部和尾部
        if file_size > sample_size * 3:
            f.seek(file_size // 2)
            hash_func.update(f.read(sample_size))
            f.seek(-sample_size, os.SEEK_END)
            hash_func.update(f.read(sample_size))
    return hash_func.hexdigest()


def find_video_files(root_dir):
    """递归查找所有视频文件"""
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.mpeg', '.mpg', '.m4v', '.3gp', '.webm']
    video_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() in video_extensions:
                video_files.append(os.path.join(dirpath, filename))
    return video_files


def group_files_by_size(video_files):
    """按文件大小分组"""
    size_to_files = defaultdict(list)
    for file in video_files:
        file_size = os.path.getsize(file)
        size_to_files[file_size].append(file)
    return size_to_files


def find_duplicates_in_group(file_group):
    """在文件大小相同的组中查找重复文件"""
    hash_to_files = defaultdict(list)
    for file in file_group:
        try:
            file_hash = calculate_file_hash(file)
            hash_to_files[file_hash].append(file)
        except Exception as e:
            print(f"Error processing file {file}: {e}")
    # 过滤出重复的文件
    duplicates = {hash_val: files for hash_val, files in hash_to_files.items() if len(files) > 1}
    return duplicates


def mark_and_delete_duplicates(duplicates):
    """标记并删除重复的视频文件"""
    for hash_val, files in duplicates.items():
        print(f"Duplicate files with hash {hash_val}:")
        for i, file in enumerate(files):
            if i == 0:
                print(f"  Keep: {file}")
            else:
                print(f"  Delete: {file}")
                os.remove(file)


def main(root_dir):
    # 查找所有视频文件
    video_files = find_video_files(root_dir)
    print(f"Found {len(video_files)} video files.")

    # 按文件大小分组
    size_to_files = group_files_by_size(video_files)
    print(f"Grouped into {len(size_to_files)} size groups.")

    # 使用多进程并行处理每个文件大小组
    duplicates = {}
    with Pool(cpu_count()) as pool:
        results = pool.map(find_duplicates_in_group, size_to_files.values())
        for result in results:
            duplicates.update(result)

    print(f"Found {len(duplicates)} sets of duplicates.")

    # 标记并删除重复的视频文件
    mark_and_delete_duplicates(duplicates)


if __name__ == "__main__":
    root_directory = "/path/to/your/video/folder"  # 替换为你的视频文件夹路径
    main(root_directory)
