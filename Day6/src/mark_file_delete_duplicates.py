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
    video_extensions = ['.mp4', '.swf', '.flv', '.mp3', '.wav', '.wma', '.wmv', '.mid', '.avi', '.mpg', '.asf', '.rm', '.rmvb', '.mkv', '.mov', '.ts', '.mpeg', '.mts', '.3gp', '.m4a', '.m4b', '.m4p']
    return find_files_by_extension(root_dir, video_extensions)


def find_image_files(root_dir):
    """递归查找所有图片文件"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    return find_files_by_extension(root_dir, image_extensions)


def find_document_files(root_dir):
    """递归查找所有文档文件"""
    document_extensions = ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.apk']
    return find_files_by_extension(root_dir, document_extensions)


def find_files_by_extension(root_dir, extensions):
    """递归查找指定扩展名的文件"""
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() in extensions:
                files.append(os.path.join(dirpath, filename))
    return files


def group_files_by_size(files):
    """按文件大小分组"""
    size_to_files = defaultdict(list)
    for file in files:
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
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Error deleting file {file}: {e}")


def main(root_dirs):
    all_video_files = []
    all_image_files = []
    all_document_files = []

    # # 查找所有视频文件
    # for root_dir in root_dirs:
    #     video_files = find_video_files(root_dir)
    #     all_video_files.extend(video_files)
    #     print(f"Found {len(video_files)} video files in {root_dir}.")
    #
    # # 查找所有图片文件
    # for root_dir in root_dirs:
    #     image_files = find_image_files(root_dir)
    #     all_image_files.extend(image_files)
    #     print(f"Found {len(image_files)} image files in {root_dir}.")

    # 查找所有文档文件
    for root_dir in root_dirs:
        document_files = find_document_files(root_dir)
        all_document_files.extend(document_files)
        print(f"Found {len(document_files)} document files in {root_dir}.")

    print(f"Total found {len(all_video_files)} video files across all directories.")
    print(f"Total found {len(all_image_files)} image files across all directories.")
    print(f"Total found {len(all_document_files)} document files across all directories.")

    # 按文件大小分组
    size_to_video_files = group_files_by_size(all_video_files)
    size_to_image_files = group_files_by_size(all_image_files)
    size_to_document_files = group_files_by_size(all_document_files)
    print(f"Grouped into {len(size_to_video_files)} size groups for videos.")
    print(f"Grouped into {len(size_to_image_files)} size groups for images.")
    print(f"Grouped into {len(size_to_document_files)} size groups for documents.")

    # 使用多进程并行处理每个文件大小组
    duplicates = {}
    with Pool(cpu_count()) as pool:
        video_results = pool.map(find_duplicates_in_group, size_to_video_files.values())
        image_results = pool.map(find_duplicates_in_group, size_to_image_files.values())
        document_results = pool.map(find_duplicates_in_group, size_to_document_files.values())
        for result in video_results + image_results + document_results:
            duplicates.update(result)

    print(f"Found {len(duplicates)} sets of duplicates.")

    # 标记并删除重复的文件
    mark_and_delete_duplicates(duplicates)


if __name__ == "__main__":
    root_directories = ["X:\\WeGame", "Y:\\video", "Z:\\downloads", "Z:\\videos", "F:\\迅雷下载","F:\\win", "G:\\新建文件夹","L:\\图书","M:\\学习文档"]  # 替换为你的文件夹路径列表
    main(root_directories)
