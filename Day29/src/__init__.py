import os

from PIL import Image


def convert_images_to_jpg(folder_path):
    # 支持的图片格式
    supported_formats = {'png', 'jpg', 'jpeg'}

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, filename)

        # 检查是否为文件
        if os.path.isfile(file_path):
            # 获取文件扩展名
            _, ext = os.path.splitext(filename)
            ext = ext.lower()[1:]  # 去掉点号并转换为小写

            # 如果不是支持的格式，则进行转换
            if ext not in supported_formats:
                try:
                    with Image.open(file_path) as img:
                        # 保存为JPG格式
                        new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                        img.save(new_file_path, 'JPEG')
                        print(f'Converted {filename} to {os.path.basename(new_file_path)}')

                        # 删除原文件
                        os.remove(file_path)
                        print(f'Removed original file {filename}')
                except Exception as e:
                    print(f'Error converting {filename}: {e}')


if __name__ == '__main__':
    # 使用示例
    folder_path = 'D:\project\github\Python-learn\Day25\src'
    convert_images_to_jpg(folder_path)
