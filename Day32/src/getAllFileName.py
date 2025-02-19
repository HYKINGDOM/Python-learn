import os

def get_file_names_as_string(folder_path):
    # 检查指定的文件夹路径是否存在
    if not os.path.exists(folder_path):
        print(f"指定的文件夹 {folder_path} 不存在。")
        return

    # 初始化一个空列表，用于存储文件名
    file_names = []

    # 遍历指定文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 使用 os.path.splitext 分离文件名和扩展名，取文件名部分
            name_without_ext = os.path.splitext(file)[0]
            # 将不包含后缀的文件名添加到列表中
            file_names.append(name_without_ext)

    # 将文件名列表转换为字符串，用逗号和空格分隔
    file_names_string = ",".join(file_names)
    return file_names_string

if __name__ == '__main__':

    # 指定文件夹路径
    folder_path = "D:\\server-log\\newfile"
    # 调用函数获取文件名组成的字符串
    result = get_file_names_as_string(folder_path)
    if result:
        print(result)