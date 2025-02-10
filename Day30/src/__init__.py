from DrissionPage import Chromium

if __name__ == '__main__':
    # 指定要解析的网址
    url = 'https://juejin.cn'  # 替换为你想要解析的网址

    tab = Chromium().latest_tab
    # 隐藏浏览器窗口
    tab.set.window.hide()
    tab.get(url)
    tab.scroll.to_bottom()

    # 在页面中查找所有元素，获取其静态版本
    ele_list = tab.eles('tag:a')

    # 基础URL
    base_url = 'https://juejin.cn'

    # 提取所有的<a>标签的href属性
    links = []
    for ele in ele_list:
        href = ele.attr('href')
        # 拼接基础URL和相对路径
        if href:
            links.append(href)

    # 打印所有的链接
    for link in links:
        print(link)
