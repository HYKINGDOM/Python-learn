import flet as ft
import time
import threading
from datetime import datetime


def main(page: ft.Page):
    page.title = "时间显示器"

    # 创建一个文本控件来显示当前时间
    timer_text = ft.Text(
        size=20,
        text_align=ft.TextAlign.CENTER,  # 文字居中对齐
        width=page.width * 0.8  # 占用页面80%宽度
    )

    # 时间更新标志
    timer_running = True

    # 更新时间显示的函数
    def update_timer():
        while timer_running:
            # 获取当前时间并格式化为年月日时分秒
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            timer_text.value = formatted_time
            page.update()
            time.sleep(1)  # 每秒更新一次

    # 将控件添加到页面，并设置居中对齐
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[timer_text],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,  # 垂直居中
                expand=True
            ),
            expand=True
        )
    )
    
    # 启动时间更新线程
    timer_thread = threading.Thread(target=update_timer, daemon=True)
    timer_thread.start()


ft.app(target=main)
