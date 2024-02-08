from DrissionPage import SessionPage



if __name__ == '__main__':

    page = SessionPage()
    url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
    save_path = r'C:\download'

    res = page.download(url, save_path)
    print(res)