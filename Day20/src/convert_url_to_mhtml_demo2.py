import os
from email.message import EmailMessage

from DrissionPage import SessionPage

from DrissionPage import ChromiumPage

#https://drissionpage.cn/ChromiumPage/get_page_info
def download_resource(session, url):
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
    # 初始化 drissionpage 会话
    chrome = ChromiumPage()
    chrome.set.load_mode.normal()
    chrome.get(url)


    # 获取网页 HTML 内容
    html_content = chrome.html
    title = chrome.title

    # 清理标题
    title = title.strip() if title else "Untitled"
    title = "".join(c if c.isalnum() or c in (' ', '.', '-') else '_' for c in title)

    # 创建 MHTML 文件
    msg = EmailMessage()
    msg['Subject'] = 'MHTML Export of: ' + url
    msg['From'] = 'webpage-exporter@example.com'
    msg['To'] = 'archive@example.com'
    msg.add_alternative(html_content, subtype='html')

    # 处理所有资源
    base_url = url.split('#')[0]  # 去掉锚点部分
    soup = BeautifulSoup(html_content, 'html.parser')

    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src.startswith('http'):
            src = base_url + '/' + src.lstrip('/')
        content = download_resource(chrome, src)
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
        content = download_resource(chrome, href)
        if content is not None:
            content_type = handle_content_type(href, content)
            if content_type:
                maintype, subtype = content_type.split('/')
                cid = f"cid:{os.urandom(8).hex()}"
                msg.add_attachment(content, maintype=maintype, subtype=subtype, cid=cid)
                link['href'] = f'cid:{cid}'

    # 保存 MHTML 文件
    filename = os.path.join(output_dir, f"{title}.mhtml")
    with open(filename, 'wb') as f:
        f.write(msg.as_bytes())
    print(f"Webpage saved as {filename}")

    # 关闭浏览器会话
    chrome.quit()


if __name__ == '__main__':
    url_to_save = 'https://juejin.cn/post/7356882188997296165'  # 替换为你想保存的网页URL
    save_as_mhtml(url_to_save)
