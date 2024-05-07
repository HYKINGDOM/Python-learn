from PIL import Image
import os

# 设置图片压缩质量
quality = 85

# 设置要压缩的图片所在的目录
input_directory = 'D:\\centos\\image'
# 设置压缩后的图片保存的目录
output_directory = 'D:\\centos\\image\\compressed_images'

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 遍历目录中的所有图片文件
for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        # 图片文件的完整路径
        img_path = os.path.join(input_directory, filename)
        # 读取图片
        img = Image.open(img_path)

        # 获取图片的格式
        img_format = img.format

        # 设置压缩后的图片文件名和路径
        compressed_img_path = os.path.join(output_directory, f'compressed_{filename}')

        # 使用指定质量进行压缩
        img.save(compressed_img_path, format=img_format, quality=quality)

        print(f'Image {filename} has been compressed and saved to {compressed_img_path}')

print('Batch compression completed.')
