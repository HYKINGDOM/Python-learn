import os

import hashlib


def get_file_hash(filepath):
    """
    计算文件的哈希值
    """
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # 逐块读取文件并更新哈希值
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def remove_duplicate_files(directory):
    """
    删除指定目录下的重复文件只保留一个
    """
    file_dict = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_hash = get_file_hash(filepath)
            if file_hash in file_dict:
                # 如果是重复文件，删除该文件
                os.remove(filepath)
            else:
                # 记录非重复文件及其哈希值
                file_dict[file_hash] = filepath


if __name__ == "__main__":
    directory = input("D:\centos")
    remove_duplicate_files(directory)
    print("处理完成！")
