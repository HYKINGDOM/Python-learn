import os

from duplicates import dupfinder

# 文件夹路径
folder_path = 'D:\centos'


def find_duplicate_files(folder_path):
    duplicates = dupfinder.Path(folder_path)
    return duplicates


def delete_duplicate_files(duplicate_files):
    for duplicate_list in duplicate_files:
        # 保留第一个文件，删除其他重复文件
        for file_path in duplicate_list[1:]:
            os.remove(file_path)


if __name__ == '__main__':
    # 查找重复文件
    duplicate_files = find_duplicate_files(folder_path)

    for duplicate_list in duplicate_files:
        # 保留第一个文件，删除其他重复文件
        for file_path in duplicate_list:
            print(file_path)

    # 删除重复文件
    # delete_duplicate_files(duplicate_files)
