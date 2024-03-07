import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os


class TestAc:
    def __init__(self):
        # 网站的基本 URL
        self.local_url = "https://www.ciyuanjie.cn"
        # 图像部分的 URL
        self.jx_local_url = "https://www.ciyuanjie.cn/cosplay"

    def run_threads(self):
        # 运行 pImage 方法
        self.p_image()

    def p_image(self):
        url = self.jx_local_url
        response = requests.get(url)
        doc = BeautifulSoup(response.text, 'html.parser')

        # 获取总页数
        tag = doc.find_all(class_="page-numbers")
        e = tag[-2]
        page_text = e.text
        page_sum = int(''.join(filter(str.isdigit, page_text)))

        # 存储所有页面 URL
        page_url_list = [f"{url}/page_{i}.html" for i in range(page_sum + 1)]

        # 并行处理每个页面
        with ThreadPoolExecutor(max_workers=16) as executor:
            executor.map(self.local_page_url, page_url_list)

    def set_jx_local_url(self, jx_local_url):
        self.jx_local_url = jx_local_url

    def get_jx_local_url(self):
        return self.jx_local_url

    def local_page_url(self, url):
        response = requests.get(url)
        doc = BeautifulSoup(response.text, 'html.parser')

        # 获取页面上的所有链接
        links = [f"{self.local_url}{a['href']}" for a in doc.select("#index_ajax_list .kzpost-data a")]

        # 并行处理每个链路
        with ThreadPoolExecutor(max_workers=16) as executor:
            executor.map(self.image_download, links)

    def image_download(self, url):
        response = requests.get(url)
        doc = BeautifulSoup(response.text, 'html.parser')

        # 提取图像链接
        image_links = [img['src'] for img in doc.select("img.aligncenter")]

        # 从页面中提取标题
        title = doc.find("title").text

        # 下载图片
        self.download_images(image_links, title)

    def download_images(self, image_links, title):
        # 定义文件夹路径
        folder_path = os.path.join("D:\\maiz\\Images",
                                   title)

        try:
            os.makedirs(folder_path, exist_ok=True)
            for url in image_links:
                redirected = requests.head(url, allow_redirects=True).url
                file_name = os.path.join(folder_path, os.path.basename(redirected).replace("/", "_"))
                with open(file_name, 'wb') as file:
                    file.write(requests.get(redirected).content)
                print("Saved successfully:", file_name)
        except Exception as e:
            print(f"Error downloading images: {e}")


if __name__ == "__main__":
    # 创建 TestAc 实例并运行线程
    test_ac = TestAc()
    test_ac.run_threads()