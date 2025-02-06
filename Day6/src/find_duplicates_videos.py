import hashlib
import os
from collections import defaultdict


def get_all_video_files(root_dirs, video_extensions=None):
    """
    遍历指定目录列表，返回所有视频文件的完整路径列表
    :param root_dirs: 列表，每个元素是一个根目录
    :param video_extensions: 指定的视频文件扩展名列表（小写，不含点），例如：['mp4', 'avi', 'mkv']
    """
    if video_extensions is None:
        # 根据需要补充更多格式
        video_extensions = ['mp4', 'avi', 'mkv', 'mov', 'flv', 'wmv', 'mpeg', 'mpg', 'rmvb', '3gp']

    video_files = []
    for root in root_dirs:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower().lstrip('.')
                if ext in video_extensions:
                    full_path = os.path.join(dirpath, filename)
                    video_files.append(full_path)
    return video_files


def group_by_size(file_list):
    """
    按文件大小分组
    返回：{size: [file_path1, file_path2, ...]}
    """
    size_dict = defaultdict(list)
    for file_path in file_list:
        try:
            size = os.path.getsize(file_path)
            size_dict[size].append(file_path)
        except Exception as e:
            print(f"获取文件大小失败 {file_path}: {e}")
    return size_dict


def compute_sample_hash(file_path, sample_size=4096):
    """
    从文件的不同位置读取部分数据，拼接后计算 SHA-256 哈希
    :param sample_size: 每个位置读取的数据量（字节数）
    :return: 十六进制哈希字符串
    """
    file_size = os.path.getsize(file_path)
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            # 读取开头
            start_data = f.read(sample_size)
            hash_obj.update(start_data)

            # 如果文件足够大，再读取中间和结尾
            if file_size > sample_size * 3:
                # 中间位置读取
                mid_pos = file_size // 2
                f.seek(mid_pos)
                mid_data = f.read(sample_size)
                hash_obj.update(mid_data)

                # 结尾读取
                f.seek(max(file_size - sample_size, 0))
                end_data = f.read(sample_size)
                hash_obj.update(end_data)
            else:
                # 如果文件比较小，直接读取全部内容
                f.seek(0)
                data = f.read()
                hash_obj = hashlib.sha256(data)
    except Exception as e:
        print(f"读取文件失败 {file_path}: {e}")
        return None
    return hash_obj.hexdigest()


def compute_full_hash(file_path, block_size=65536):
    """
    分块读取全文件数据计算 SHA-256 哈希
    :param block_size: 每次读取的字节数
    :return: 十六进制哈希字符串
    """
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(block_size)
                if not data:
                    break
                hash_obj.update(data)
    except Exception as e:
        print(f"全量计算文件哈希失败 {file_path}: {e}")
        return None
    return hash_obj.hexdigest()


def find_duplicates(root_dirs):
    """
    查找重复的视频文件
    返回一个字典：{最终哈希: [file1, file2, ...]}，列表中第一个为保留文件，其余为重复待删除的文件
    """
    video_files = get_all_video_files(root_dirs)
    print(f"总共找到 {len(video_files)} 个视频文件。")

    # 1. 按文件大小分组
    size_groups = group_by_size(video_files)
    potential_duplicates = []
    for size, files in size_groups.items():
        if len(files) > 1:
            potential_duplicates.extend(files)
    print(f"经过大小筛选，潜在重复文件数：{len(potential_duplicates)}")

    # 2. 对同一大小的文件，计算采样哈希分组
    sample_hash_dict = defaultdict(list)
    for file_path in potential_duplicates:
        sample_hash = compute_sample_hash(file_path)
        if sample_hash:
            sample_hash_dict[(os.path.getsize(file_path), sample_hash)].append(file_path)

    # 3. 对采样哈希相同的，再进行精确对比
    duplicates = {}  # key: 最终全量哈希, value: list of file paths
    for (size, sample_hash), files in sample_hash_dict.items():
        if len(files) < 2:
            continue  # 唯一文件不用处理
        # 对此组文件计算全文件哈希（可选，如果对采样哈希的准确性有足够信心，可以直接认为采样相同就重复）
        full_hash_dict = defaultdict(list)
        for file_path in files:
            full_hash = compute_full_hash(file_path)
            if full_hash:
                full_hash_dict[full_hash].append(file_path)
        for full_hash, file_list in full_hash_dict.items():
            if len(file_list) > 1:
                duplicates[full_hash] = file_list

    return duplicates


def delete_duplicates(duplicates, keep_first=True):
    """
    删除重复文件，默认保留每组的第一个文件
    :param duplicates: 字典，key 为文件哈希，value 为文件路径列表
    :param keep_first: 是否保留列表中的第一个文件
    """
    total_deleted = 0
    for file_hash, file_list in duplicates.items():
        # 排序可以根据文件创建时间或其它条件排序，此处直接用列表顺序
        files_to_delete = file_list[1:] if keep_first else file_list
        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                print(f"已删除：{file_path}")
                total_deleted += 1
            except Exception as e:
                print(f"删除文件失败 {file_path}: {e}")
    print(f"总共删除了 {total_deleted} 个重复文件。")


if __name__ == '__main__':
    # 设置要扫描的根目录列表（可同时设置多个目录）
    roots = [r"/path/to/videos"]

    # 查找重复文件（该操作会根据文件大小、采样哈希、全量哈希逐步筛选）
    duplicates = find_duplicates(roots)
    print(f"发现 {len(duplicates)} 组重复文件。")
    for file_hash, files in duplicates.items():
        print(f"哈希：{file_hash} 对应的文件：")
        for f in files:
            print(f"    {f}")

    # 若确认后删除重复文件（保留每组的第一个文件），请取消下面注释
    # delete_duplicates(duplicates, keep_first=True)
