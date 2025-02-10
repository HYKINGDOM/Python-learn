import hashlib
import os
import re
import time

import requests
from DrissionPage import Chromium


def clean_filename(filename):
    # 移除或替换无效字符
    return re.sub(r'[\\/*?:"<>|]', '', filename)


def calculate_hash(value, length):
    """计算哈希值并截取指定长度"""
    hash_object = hashlib.md5(value.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[:length]


def generate_time_based_hash(length):
    """生成基于时间戳的哈希值并截取指定长度"""
    timestamp = str(time.time())
    hash_object = hashlib.md5(timestamp.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[:length]


if __name__ == '__main__':

    tab = Chromium().latest_tab
    # 隐藏浏览器窗口
    tab.set.window.hide()
    tab.get('https://juejin.cn/post/7441617140229554214')
    print(tab.title)

    tab.scroll.to_bottom()

    # 在页面中查找所有元素，获取其静态版本
    ele_list = tab.eles('tag:img')

    for ele in ele_list:
        img_url = ele.attr('src')
        print(img_url)
        # 判断图片是否为空字符串
        if not img_url:
            print("Error: img_url is an empty string.")
            continue
        # 下载图片
        try:
            response = requests.get(img_url)
            response.raise_for_status()  # 检查请求是否成功
            print("Image fetched successfully!")
            if response.status_code == 200:
                # 计算 tab.title 的五位长度的哈希值
                title_hash = calculate_hash(tab.title, 5)
                # 生成图片按时间增长的 11 位哈希值
                time_hash = generate_time_based_hash(11)
                # 构建新的文件名
                img_extension = os.path.splitext(os.path.basename(img_url))[1]
                new_img_name = f"{title_hash}-{time_hash}{img_extension}"
                new_img_name = clean_filename(new_img_name)
                with open(new_img_name, 'wb') as f:
                    f.write(response.content)
        except requests.exceptions.MissingSchema as e:
            print(f"Error: {e} , http url :{img_url}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP Error: {e}")
