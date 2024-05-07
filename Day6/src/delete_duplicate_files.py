import hashlib
import os
import pathlib
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def open_file_safely(file_path, mode):
    """打开文件并优雅地处理权限和不存在的问题"""
    try:
        return open(file_path, mode)
    except FileNotFoundError:
        logging.error(f"文件找不到: {file_path}")
        raise
    except PermissionError:
        logging.error(f"没有权限访问: {file_path}")
        raise


def calculate_file_hash(file_path, hash_factory=hashlib.md5, chunk_size=2 ** 20):
    """使用给定的哈希算法计算文件的哈希值"""
    h = hash_factory()
    with open_file_safely(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.digest()


def find_duplicate_files(folder_path):
    file_hash_dict = {}

    for root, dirs, files in os.walk(str(folder_path)):
        for file in files:
            file_path = pathlib.Path(os.path.join(root, file))
            file_size = file_path.stat().st_size
            logging.info(f"文件大小: {file_size}")

            file_hash = calculate_file_hash(file_path)

            if file_hash in file_hash_dict:
                file_hash_dict[file_hash].append(str(file_path))
            else:
                file_hash_dict[file_hash] = [str(file_path)]

    return [value for key, value in file_hash_dict.items() if len(value) > 1]


def find_duplicate_files_by_hash(file_list):
    file_hash_dict = {}
    for file_path, file_hash in file_list:
        if file_hash in file_hash_dict:
            file_hash_dict[file_hash].append((file_path, datetime.fromtimestamp(os.path.getctime(file_path))))
        else:
            file_hash_dict[file_hash] = [(file_path, datetime.fromtimestamp(os.path.getctime(file_path)))]

    earliest_time = None
    earliest_files = []
    for file_list_with_ctime in file_hash_dict.values():
        for file_path, ctime in file_list_with_ctime:
            if earliest_time is None or ctime < earliest_time:
                earliest_time = ctime
                earliest_files = [(file_path, ctime)]
            elif ctime == earliest_time:
                earliest_files.append((file_path, ctime))

    return [file_path for file_path, _ in earliest_files]


def delete_duplicate_files(duplicate_files, dry_run=False):
    for duplicate_list in duplicate_files:
        earliest_file_path = None
        for file_path_list in duplicate_list:
            if earliest_file_path is None:
                earliest_file_path = file_path_list
            else:
                try:
                    logging.info(f"待删除文件: {file_path_list}")
                    if not dry_run:
                        os.remove(file_path_list)
                        logging.info(f"已删除文件: {file_path_list}")
                except OSError as e:
                    logging.error(f"删除文件时出现错误: {file_path_list}")
                    logging.error(e)
                    # 决定是否继续尝试删除其他文件或中断


if __name__ == '__main__':
    folder_path = pathlib.Path('D:\\centos\\video')
    duplicate_files = find_duplicate_files(folder_path)
    for file_list in duplicate_files:
        for file_path in file_list:
            logging.info(f"检索到的重复文件: {file_path}")
    delete_duplicate_files(duplicate_files, dry_run=False)
