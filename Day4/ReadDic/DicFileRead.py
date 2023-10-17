import os
import shutil

# 示例用法
source_folder = 'D:\centos\download'
destination_folder = 'D:\centos'



def organize_files(source_folder, destination_folder):
    # 遍历源文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()  # 获取文件扩展名（转换为小写）

            # 根据文件类型进行分类
            if file_extension in ['.mp4', '.mkv', '.m4v']:
                dest_folder = os.path.join(destination_folder, '视频')
            elif file_extension in ['.mp3', '.wav']:
                dest_folder = os.path.join(destination_folder, '音频')
            elif file_extension in ['.png', '.jpg', '.gif', '.webp']:
                dest_folder = os.path.join(destination_folder, '图片')
            elif file_extension in ['.exe', '.msi', '.iso']:
                dest_folder = os.path.join(destination_folder, '安装包')
            elif file_extension in ['.pdf', '.doc', '.docx', 'xls', '.pptx', '.xls', '.xlsx', '.csv', '.txt', '.mhtml']:
                dest_folder = os.path.join(destination_folder, '文档')
            elif file_extension in ['.zip', '.7z', '.rar']:
                dest_folder = os.path.join(destination_folder, '压缩包')
            elif file_extension in ['.xml', '.sql', '.json', '.log', '.jar', '.yaml', '.yml', '.gz']:
                dest_folder = os.path.join(destination_folder, '开发')
            else:
                continue  # 跳过不需要处理的文件类型

            # 创建目标文件夹（如果不存在）
            os.makedirs(dest_folder, exist_ok=True)

            # 移动文件到目标文件夹（处理同名文件重命名）
            dest_file_path = os.path.join(dest_folder, file)
            if os.path.exists(dest_file_path):
                filename, file_extension = os.path.splitext(file)
                counter = 1
                while True:
                    new_filename = f"{filename}_{counter}{file_extension}"
                    new_file_path = os.path.join(dest_folder, new_filename)
                    if not os.path.exists(new_file_path):
                        dest_file_path = new_file_path
                        break
                    counter += 1
            shutil.move(file_path, dest_file_path)

    # 删除空文件夹
    for root, dirs, files in os.walk(source_folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # 如果文件夹为空
                os.rmdir(dir_path)


if __name__ == '__main__':
    organize_files(source_folder, destination_folder)
