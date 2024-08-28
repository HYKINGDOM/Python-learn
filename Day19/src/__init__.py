import os

#遍历一个文件夹下所有的.java文件,找到行数最多的前三个文件, 输出其文件名和文件路径

def find_top_java_files(directory, top_n=3):
    # 存储文件名和行数
    file_line_counts = []

    # 遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = sum(1 for line in f)
                file_line_counts.append((file, file_path, line_count))

    # 按行数排序并获取前三个
    top_files = sorted(file_line_counts, key=lambda x: x[2], reverse=True)[:top_n]

    # 输出结果
    for file_name, file_path, line_count in top_files:
        print(f"文件名: {file_name}, 路径: {file_path}, 行数: {line_count}")



if __name__ == '__main__':
    find_top_java_files("D:\\project")