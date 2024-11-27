from DrissionPage import Chromium

if __name__ == '__main__':

    tab = Chromium().latest_tab
    # 隐藏浏览器窗口
    tab.set.window.hide()
    tab.get('https://juejin.cn/post/7441617140229554214')
    print(tab.title)

    tab.scroll.to_bottom()

    # 在页面中查找元素，获取其静态版本
    ele1 = tab.s_ele('tag:img')

    print(ele1.attr('src'))

