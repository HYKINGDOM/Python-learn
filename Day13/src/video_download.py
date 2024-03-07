import re
import requests
import os
from tqdm import tqdm

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"}


# 抖音视频无水印
def videos(surl):
    print('正在解析抖音视频链接')
    # 获取video_id （重定向后的链接会变化具体我也没弄清楚就做了两种判断）
    if len(surl) > 60:
        id = re.search(r'video/(\d.*)/', surl).group(1)
    else:
        id = re.search(r'video/(\d.*)', surl).group(1)
    # print(id)
    # 获取json数据
    u_id = "https://m.douyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&a_bogus=".format(id)
    v_rs = requests.get(url=u_id, headers=header).json()
    # titles = v_rs['item_list'][0]['desc']
    # 截取文案
    titles = re.search(r'^(.*?)[；;。.#]', v_rs['item_list'][0]['desc']).group(1)
    # print(titles)
    # 创建video文件夹
    if not os.path.exists('douyin/video'):
        os.makedirs('douyin/video')
    # 获取uri参数
    req = v_rs['item_list'][0]['video']['play_addr']['uri']
    # print("vvvvvv", req)
    print('正在下载无水印视频')
    # 下载无水印视频
    v_url = "https://www.douyin.com/aweme/v1/play/?video_id={}".format(req)
    v_req = requests.get(url=v_url, headers=header, stream=True)
    # 写入文件
    # 拿到文件的长度，并把total初始化为0
    total = int(v_req.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(f'douyin/video/{titles}.mp4', 'wb') as file, tqdm(
            desc=f'{titles}.mp4',
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in v_req.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


# 抖音图片无水印
def pics(surl):
    print('正在解析抖音图片链接')
    # 获取id
    if len(surl) > 60:
        pid = re.search(r'note/(\d.*)/', surl).group(1)
    else:
        pid = re.search(r'note/(\d.*)', surl).group(1)
    # 获取json数据
    p_id = "https://m.douyin.com/web/api/v2/aweme/iteminfo/?reflow_source=reflow_page&item_ids={}&a_bogus=".format(pid)
    # print(p_id)
    p_rs = requests.get(url=p_id, headers=header).json()
    # print(p_rs)
    # 拿到images下的原图片
    images = p_rs['item_list'][0]['images']
    # 获取文案
    ptitle = re.search(r'^(.*?)[；;。.#]', p_rs['item_list'][0]['desc']).group(1).strip()
    # 创建pic文件夹
    if not os.path.exists('douyin/pic'):
        os.makedirs('douyin/pic')
    if not os.path.exists(f'douyin/pic/{ptitle}'):
        os.makedirs(f'douyin/pic/{ptitle}')
    print('正在下载无水印图片')
    # 下载无水印照片(遍历images下的数据)
    for i, im in enumerate(images):
        # 每一条数据下面都有四个原图链接这边用的是第一个
        p_req = requests.get(url=im['url_list'][0])
        # print(p_req)
        # 保存图片
        # 拿到文件的长度，并把total初始化为0
        total = int(p_req.headers.get('content-length', 0))
        # 打开当前目录的fname文件(名字你来传入)
        # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
        with open(f'douyin/pic/{ptitle}/{str(i + 1)}.jpg', 'wb') as file, tqdm(
                desc=f'{ptitle + str(i + 1)}.jpg',
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in p_req.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)


# 皮皮虾无水印视频
def ppx(surl):
    print('正在解析皮皮虾视频链接')
    xid = re.search(r'item/(.*)[?]', surl).group(1)
    # print(xid)
    pp_url = "https://h5.pipix.com/bds/webapi/item/detail/?item_id={}".format(xid)
    pp_req = requests.get(url=pp_url, headers=header).json()
    # print(pp_req)
    p_video = pp_req['data']['item']['comments'][0]['item']['video']['video_high']['url_list'][0]['url']
    if not os.path.exists('ppx/video'):
        os.makedirs('ppx/video')
    print('正在下载皮皮虾无水印视频')
    pp_v = requests.get(url=p_video, headers=header)
    # 拿到文件的长度，并把total初始化为0
    total = int(pp_v.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(f'ppx/video/{xid}.mp4', 'wb') as file, tqdm(
            desc=f'{xid}.mp4',
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in pp_v.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


# 最右无水印
def zy(s_html, surl):
    # print(surl)
    print('正在解析最右视频链接')
    # 获取视频名称
    z_name = re.search(r'pid=(.*?)&', surl).group(1)
    if not os.path.exists('zuiyou/video'):
        os.makedirs('zuiyou/video')
    print('正在下载最右无水印视频')
    # 请求无水印视频地址
    z_url = re.search(r'x5-video-player-fullscreen="false" src="(.*)"\sposter=', s_html).group(1)
    z_res = requests.get(url=z_url, headers=header)
    # 拿到文件的长度，并把total初始化为0
    total = int(z_res.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(f'zuiyou/video/{z_name}.mp4', 'wb') as file, tqdm(
            desc=f'{z_name}.mp4',
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in z_res.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


if __name__ == '__main__':
    print("抖音支持视频分享链接和图文分享链接")
    print("皮皮虾和最右仅支持视频分享链接")
    shares = input("请输入分享链接并按下回车键：")
    if re.search(r'/v.douyin.com/', shares) != None:
        # 提取分享链接后面的链接
        share = re.search(r'/v.douyin.com/(.*?)/', shares).group(1)
        # 请求链接
        share_url = "https://v.douyin.com/{}/".format(share)
    elif re.search(r'h5.pipix.com/', shares) != None:
        # 请求链接
        share_url = "{}".format(shares)
    elif re.search(r'share.xiaochuankeji.cn/', shares) != None:
        # 提取分享链接后面的链接
        share = re.search(r'>\s(.*)', shares).group(1)
        # 请求链接
        share_url = "{}".format(share)
    # print(share_url)
    s_html = requests.get(url=share_url, headers=header)
    # 获取重定向后的视频id
    surl = s_html.url
    # print(s_html.status_code)
    # print(surl)
    # 判断链接类型为视频分享类型
    if re.search(r'/video', surl) != None:
        videos(surl)
        quit = input('下载完成，按回车键退出程序。')
    # 判断链接类型为图集分享类型
    elif re.search(r'/note', surl) != None:
        pics(surl)
        quit = input('下载完成，按回车键退出程序。')
    elif re.search(r'h5.pipix.com/', surl) != None:
        ppx(surl)
        quit = input('下载完成，按回车键退出程序。')
    elif re.search(r'share.xiaochuankeji.cn/', shares) != None:
        zy(s_html.text, surl)
        quit = input('下载完成，按回车键退出程序。')
    else:
        quit = input('解析失败，按回车键退出程序。')