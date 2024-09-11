import os
from email.message import EmailMessage
from mimetypes import guess_type

import requests
from bs4 import BeautifulSoup


def download_resource(url, session):
    try:
        response = session.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to download resource from {url} (status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Error downloading resource from {url}: {e}")
        return None


def handle_content_type(url, content):
    content_type = guess_type(url)[0]
    if content_type:
        return content_type
    else:
        # 尝试根据内容判断类型
        if content.startswith(b'<?xml'):
            return 'application/xml'
        elif content.startswith(b'<!DOCTYPE html'):
            return 'text/html'
        elif content.startswith(b'<html'):
            return 'text/html'
        elif content.startswith(b'<!DOCTYPE'):
            return 'text/html'
        elif content.startswith(b'<!'):
            return 'text/html'
        elif content.startswith(b'{'):
            return 'application/json'
        elif content.startswith(b'['):
            return 'application/json'
        elif content.startswith(b'GIF89a'):
            return 'image/gif'
        elif content.startswith(b'\x89PNG\r\n\x1a\n'):
            return 'image/png'
        elif content.startswith(b'\xff\xd8\xff'):
            return 'image/jpeg'
        elif content.startswith(b'%PDF-'):
            return 'application/pdf'
        else:
            print(f"Failed to determine content type for {url}")
            return None


def save_as_mhtml(url, output_dir='.'):
    # 获取网页内容
    session = requests.Session()
    response = session.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    # 解析HTML以获取网页标题
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else "Untitled"
    title = "".join(c if c.isalnum() or c in (' ', '.', '-') else '_' for c in title)

    # 创建MHTML文件
    msg = EmailMessage()
    msg['Subject'] = 'MHTML Export of: ' + url
    msg['From'] = 'webpage-exporter@example.com'
    msg['To'] = 'archive@example.com'
    msg.add_alternative(response.text, subtype='html')

    # 处理所有资源
    base_url = url.split('#')[0]  # 去掉锚点部分
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src.startswith('http'):
            src = base_url + '/' + src.lstrip('/')
        content = download_resource(src, session)
        if content is not None:
            content_type = handle_content_type(src, content)
            if content_type:
                maintype, subtype = content_type.split('/')
                cid = f"cid:{os.urandom(8).hex()}"
                msg.add_attachment(content, maintype=maintype, subtype=subtype, cid=cid)
                img['src'] = f'cid:{cid}'

    for link in soup.find_all('link'):
        href = link.get('href', '')
        if not href.startswith('http'):
            href = base_url + '/' + href.lstrip('/')
        content = download_resource(href, session)
        if content is not None:
            content_type = handle_content_type(href, content)
            if content_type:
                maintype, subtype = content_type.split('/')
                cid = f"cid:{os.urandom(8).hex()}"
                msg.add_attachment(content, maintype=maintype, subtype=subtype, cid=cid)
                link['href'] = f'cid:{cid}'

    # 保存MHTML文件
    filename = os.path.join(output_dir, f"{title}.mhtml")
    with open(filename, 'wb') as f:
        f.write(msg.as_bytes())
    print(f"Webpage saved as {filename}")


if __name__ == '__main__':
    url_to_save = 'https://juejin.cn/post/7356882188997296165'  # 替换为你想保存的网页URL
    save_as_mhtml(url_to_save)
