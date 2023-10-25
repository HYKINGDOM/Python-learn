import hashlib
import mimetypes
import os

# 文件夹路径
folder_path = 'D:\centos\安装包'


def get_file_hash(file_path):
    # 读取文件内容并计算哈希值
    with open(file_path, 'rb') as file:
        data = file.read()
        file_hash = hashlib.sha256(data).hexdigest()
    return file_hash


def checksum(file_path, hash_factory=hashlib.md5, chunk_num_blocks=128):
    h = hash_factory()
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_num_blocks * h.block_size):
            h.update(chunk)
    return h.digest()


def find_duplicate_files(folder_path):
    # 存储文件类型和对应的文件哈希值字典
    file_type_dict = {}

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # 获取文件类型
            file_type, _ = mimetypes.guess_type(file_path)

            # 如果文件类型未知，则将其归类为 "unknown"
            if file_type is None:
                file_type = "unknown"

            # 计算文件的哈希值
            file_hash = checksum(file_path)

            # 根据文件类型建立哈希值字典
            if file_type in file_type_dict:
                file_type_dict[file_type].append((file_path, file_hash))
            else:
                file_type_dict[file_type] = [(file_path, file_hash)]

    # 返回文件类型和对应的重复文件列表字典
    duplicate_files_dict = {}
    for file_type, file_list in file_type_dict.items():
        duplicate_files_dict[file_type] = find_duplicate_files_by_hash(file_list)

    return duplicate_files_dict


def find_duplicate_files_by_hash(file_list):
    # 存储哈希值和对应的文件路径
    file_hash_dict = {}

    # 遍历文件列表
    for file_path, file_hash in file_list:
        # 如果哈希值已存在，则说明是重复文件
        if file_hash in file_hash_dict:
            file_hash_dict[file_hash].append(file_path)
        else:
            file_hash_dict[file_hash] = [file_path]

    # 返回重复文件的列表
    return [file_list for file_list in file_hash_dict.values() if len(file_list) > 1]


def delete_duplicate_files(duplicate_files):
    for duplicate_list in duplicate_files.values():
        # 保留第一个文件，删除其他重复文件
        for file_path_one in duplicate_list[1:]:
            try:
                file_path = file_path_one[0]
                print(f"file_path_one: {file_path_one}")
                print(f"file_path: {file_path}")
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
            except OSError as e:
                print(f"删除文件时出现错误: {file_path}")
                print(e)


if __name__ == '__main__':
    # 查找重复文件
    duplicate_files = find_duplicate_files(folder_path)

    for file_list in duplicate_files.values():
        # 保留第一个文件，删除其他重复文件
        for file_path in file_list:
            print(file_path)

    # 删除重复文件
    delete_duplicate_files(duplicate_files)
