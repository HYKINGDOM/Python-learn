import collections
import os

import requests

# 原始数据获取URL
raw_url = 'https://image.so.com/zjl?ch=wallpaper&sn=60'

base_url = 'https://image.so.com/zjl?ch=wallpaper&sn='

# 根据开发者工具中的request header信息来设置headers
# headers的作用就是为了我们的爬虫能够模拟浏览器去查找，让系统以为是人为操作的下载的
headers = {
    'Referer': 'https://image.so.com/z?ch=wallpaper',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie': 'opqopq=173f7d9fe967fd169bfe33435088536c.1696829445; _S=856b9cf2f91ad5e1da692f192a691a6d; QiHooGUID=6FB4359779339D126046712E1097E91C.1696829445438; __guid=16527278.2329050198193150500.1696829445405.2117; test_cookie_enable=null; tracker=; __huid=11smyx8VjD6vadeTjL0uTqiR7MTGx9y3cDTkPOxKMdKcE%3D; gtHuid=1'
}

directory = './image'

# 创建命名元组类型
ImageInfo = collections.namedtuple('ImageInfo', ['pic_url', 'pic_desc'])

i = 0


## 实现爬取单张图片
def get_one_image():
    res = requests.get(raw_url, headers=headers)  # 发出get请求

    if 200 != res.status_code:
        print(res.content)
        return

    _json = res.json()  # 拿到源代码的json文件，是用列表形式
    _1_dic = _json.get('list')[1]  # 拿到第一张图片的信息
    image_url = _1_dic.get('imgurl')  # 到第一张图片的信息的url
    pic_desc = _1_dic.get('title')  # 到第一张图片的描述信息
    image_data = requests.get(image_url)  # 请求
    img = image_data.content  # 拿到图片信息

    file_path = os.path.join(directory, pic_desc + '.jpg')  # 拼接目标目录和文件名

    with open(file_path, 'wb') as f:  # 利用字节的方式进行保存图片
        f.write(img)


def save_image(pic_url, pic_desc):
    # filename = url.lstrip('http://').replace('.', '').replace('/', '').rstrip('jpg')+'.jpg'
    global i
    filename = pic_desc + '.jpg'
    filename_path = pic_desc + '/' + filename  # 修改放在指定文件夹
    # 将图片地址转化为图片文件名
    try:
        res = requests.get(pic_url)
        if res.ok:
            img = res.content
            if not os.path.exists(filename_path):  # 检查该图片是否已经下载过
                file_path = os.path.join(directory, filename)
                with open(file_path, 'wb') as f:
                    f.write(img)
                    print(filename + "图片下载完成", sep="\n")
                    i += 1
    except Exception:
        print('Failed to load the picture', sep="\n")


def get_url_to_json(start_url):
    try:
        res = requests.get(start_url, headers=headers)
        if res.ok:  # 成功访问
            return res.json()  # 返回json
        else:
            print('not ok')
            return False
    except Exception as e:
        print('Error here:\t', e)


def json_parser(json):
    if json is not None:
        news_list = json.get('list')
        if not news_list:
            return False
        for news_item in news_list:
            pic_desc = news_item.get('title')
            pic_url = news_item.get('imgurl')
            yield ImageInfo(pic_url=pic_url, pic_desc=pic_desc)


def worker(url):
    raw_json = get_url_to_json(url)  # 获取原始JSON数据
    print(raw_json)
    # 调用生成器函数并迭代获取生成的值
    for image_info in json_parser(raw_json):
        pic_url = image_info.pic_url
        pic_desc = image_info.pic_desc
        print(pic_url, pic_desc)
        save_image(pic_url, pic_desc)


if __name__ == '__main__':
    for i in range(1, 10):
        num = 30 * i
        url = base_url + str(num)
        worker(url)

    #get_one_image()
