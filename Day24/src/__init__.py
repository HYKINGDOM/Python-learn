import os

def scan_and_rename_files(directory):
    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件名长度是否大于200
            if len(file) > 50:
                # 获取完整的文件路径
                full_path = os.path.join(root, file)
                # 截取前50个字符
                new_name = file[:10]
                # 确保新文件名不与现有文件冲突
                base, extension = os.path.splitext(new_name)
                counter = 1
                while os.path.exists(os.path.join(root, new_name)):
                    new_name = f"{base}_{counter}{extension}"
                    counter += 1
                # 打印原文件名和新文件名
                print(f"Renaming '{full_path}' to '{os.path.join(root, new_name)}'")
                # 重命名文件
                os.rename(full_path, os.path.join(root, new_name))

if __name__ == '__main__':
    path = "X:\\WeGame\\视频"

    # 执行扫描和重命名
    scan_and_rename_files(path)
