import csv
import os
import requests


def download_files_from_csv(csv_file_path, download_folder):
    # 检查下载文件夹是否存在，如果不存在则创建
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # 打开 CSV 文件
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # 创建 CSV 读取器
        reader = csv.reader(file)
        # 遍历 CSV 文件的每一行
        for row in reader:
            # 提取 ID 和 URL
            id = row[0]
            url = row[1]
            try:
                # 发送 HTTP 请求下载文件
                response = requests.get(url)
                # 检查响应状态码是否为 200
                if response.status_code == 200:
                    # 构建文件保存路径
                    file_path = os.path.join(download_folder, f'{id}.pdf')
                    # 打开文件并写入内容
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print(f'Successfully downloaded {id}.pdf')
                else:
                    print(f'Failed to download {id}.pdf. Status code: {response.status_code}')
            except requests.RequestException as e:
                print(f'Error downloading {id}.pdf: {e}')

# 指定 CSV 文件路径和下载文件夹路径
csv_file_path = 'D:\\server-log\\platform_cloud_sys_oss_07.csv'
download_folder = 'D:\\server-log\\file'


if __name__ == '__main__':
# 调用函数下载文件
    download_files_from_csv(csv_file_path, download_folder)