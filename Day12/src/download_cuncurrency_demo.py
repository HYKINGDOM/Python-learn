from DrissionPage import SessionPage

from DownloadKit import DownloadKit

proxies = {
    "http": "http://localhost:7890"
}


# 文档地址 https://g1879.gitee.io/drissionpagedocs/download/DownloadKit

if __name__ == '__main__':
    url1 = 'https://github.com/jellyfin/jellyfin-android/releases/download/v2.6.0/jellyfin-android-v2.6.0-proprietary-release.apk'
    url2 = 'https://github.com/jellyfin/jellyfin-android/releases/download/v2.6.0/jellyfin-android-v2.6.0-libre-release.apk'
    save_path = r'C:\download'

    page = DownloadKit()

    page.set.block_size('30m')
    mission = page.add(url1, save_path,proxies=proxies)
    mission.wait()

    print(mission.id)  # 获取任务id
    print(mission.rate)  # 打印下载进度（百分比）
    print(mission.state)  # 打印任务状态
    print(mission.info)  # 打印任务信息
    print(mission.result)  # 打印任务结果

    print(page.get_failed_missions())

    page.add(url2, save_path, ).wait()

    print(page.get_failed_missions())