import flet as ft
import os
import datetime
import mysql.connector
import csv
import pandas as pd
from typing import Optional
import threading


class DataExportApp:
    def __init__(self):
        # 数据库连接信息
        self.db_config = {
            'host': '10.0.220.30',
            'port': 3306,
            'database': 'temp_20220629',
            'user': 'platform',
            'password': 'Platform_1314',
            'charset': 'utf8',
            'use_unicode': True,
        }
        
        # 应用状态
        self.start_date: Optional[datetime.date] = None
        self.end_date: Optional[datetime.date] = None
        self.export_dir: Optional[str] = None
        self.is_exporting = False
        
        # UI组件
        self.start_date_picker = None
        self.end_date_picker = None
        self.start_date_text = None
        self.end_date_text = None
        self.export_dir_textfield = None
        self.export_button = None
        self.log_text = None
        
    def build_ui(self, page: ft.Page):
        """构建应用UI"""
        page.title = "消耗数据导出工具"
        page.window_width = 800
        page.window_height = 600
        page.padding = 20
        page.locale = "zh"
        
        # 标题
        title = ft.Text("消耗数据导出", size=24, weight=ft.FontWeight.BOLD)
        
        # 日期选择器
        self.start_date_picker = ft.DatePicker(
            on_change=self.start_date_changed,
            first_date=datetime.datetime(2020, 1, 1),
            last_date=datetime.datetime.now(),
        )
        page.overlay.append(self.start_date_picker)
        
        self.end_date_picker = ft.DatePicker(
            on_change=self.end_date_changed,
            first_date=datetime.datetime(2020, 1, 1),
            last_date=datetime.datetime.now(),
        )
        page.overlay.append(self.end_date_picker)
        
        # 文件选择器
        self.directory_picker = ft.FilePicker(on_result=self.pick_folder_result)
        page.overlay.append(self.directory_picker)
        
        self.start_date_text = ft.Text("")
        start_date_row = ft.Row([
            ft.Text("开始时间", size=16),
            ft.OutlinedButton(
                "选择日期",
                icon=ft.Icons.CALENDAR_TODAY,
                on_click=lambda e: e.page.open(self.start_date_picker)
            ),
            self.start_date_text
        ])
        
        self.end_date_text = ft.Text("")
        end_date_row = ft.Row([
            ft.Text("结束时间", size=16),
            ft.OutlinedButton(
                "选择日期",
                icon=ft.Icons.CALENDAR_TODAY,
                on_click=lambda e: e.page.open(self.end_date_picker)
            ),
            self.end_date_text
        ])
        
        # 导出目录选择
        self.export_dir_textfield = ft.TextField(
            label="导出目录",
            read_only=True,
            expand=True,
        )
        
        export_dir_row = ft.Row([
            ft.Text("导出目录:", size=16),
            self.export_dir_textfield,
            ft.IconButton(
                icon=ft.Icons.FOLDER_OPEN,
                tooltip="选择导出目录",
                on_click=self.pick_export_dir
            )
        ])
        
        # 导出按钮
        self.export_button = ft.ElevatedButton(
            "开始导出",
            on_click=self.start_export,
            disabled=True,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.padding.symmetric(horizontal=24, vertical=12),
            )
        )
        
        button_row = ft.Row([self.export_button], alignment=ft.MainAxisAlignment.CENTER)
        
        # 日志区域
        log_title = ft.Text("执行日志:", size=18, weight=ft.FontWeight.BOLD)
        self.log_text = ft.TextField(
            multiline=True,
            read_only=True,
            min_lines=8,
            max_lines=8,
            expand=True,
        )
        
        # 布局
        page.add(
            title,
            ft.Divider(),
            start_date_row,
            end_date_row,
            export_dir_row,
            ft.Container(height=20),  # 间距
            button_row,
            ft.Container(height=20),  # 间距
            log_title,
            self.log_text,
        )
    
    def start_date_changed(self, e):
        """开始日期变更处理"""
        print(f"开始日期变更: {e.data}")
        # 将字符串转换为datetime对象
        if e.data and isinstance(e.data, str):
            date_str = e.data.split('T')[0]  # 提取日期部分
            self.start_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            self.start_date_text.value = date_str
        else:
            self.start_date = None
            self.start_date_text.value = ""
        
        self.start_date_text.update()
        self.validate_inputs()
    
    def end_date_changed(self, e):
        """结束日期变更处理"""
        print(f"结束日期变更: {e.data}")
        # 将字符串转换为datetime对象
        if e.data and isinstance(e.data, str):
            date_str = e.data.split('T')[0]  # 提取日期部分
            self.end_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            self.end_date_text.value = date_str
        else:
            self.end_date = None
            self.end_date_text.value = ""
        
        self.end_date_text.update()
        self.validate_inputs()
    
    def pick_export_dir(self, e):
        """选择导出目录"""
        print("尝试打开目录选择对话框...")
        self.directory_picker.get_directory_path()
    
    def pick_folder_result(self, e: ft.FilePickerResultEvent):
        """文件夹选择结果处理"""
        print(f"文件夹选择结果: {e.path}")
        if e.path:
            self.export_dir = e.path
            self.export_dir_textfield.value = self.export_dir
            self.export_dir_textfield.update()
            self.validate_inputs()
    
    def validate_inputs(self):
        """验证输入是否有效"""
        valid = True
        error_msg = ""
        
        # 检查日期是否已选择
        if not self.start_date or not self.end_date:
            valid = False
            error_msg = "请选择开始和结束日期"
        
        # 检查开始日期是否小于结束日期
        elif self.start_date > self.end_date:
            valid = False
            error_msg = "开始日期必须小于结束日期"
            self.log_message(error_msg)
        
        # 检查日期范围是否在一个月内
        elif (self.end_date - self.start_date).days > 31:
            valid = False
            error_msg = "日期范围不能超过一个月"
            self.log_message(error_msg)
        
        # 检查导出目录是否已选择
        if not self.export_dir:
            valid = False
            if not error_msg:
                error_msg = "请选择导出目录"
        
        # 更新导出按钮状态
        self.export_button.disabled = not valid
        self.export_button.update()
        
        if error_msg and not valid:
            self.log_message(error_msg)
    
    def log_message(self, message):
        """记录日志消息"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # 追加到日志文本框
        if self.log_text.value:
            self.log_text.value += log_entry
        else:
            self.log_text.value = log_entry
        
        self.log_text.update()
    
    def start_export(self, e):
        """开始导出数据"""
        if self.is_exporting:
            self.log_message("导出任务正在进行中，请等待完成")
            return
        
        # 再次验证输入
        self.validate_inputs()
        if self.export_button.disabled:
            return
        
        # 设置导出状态
        self.is_exporting = True
        self.export_button.disabled = True
        self.export_button.text = "导出中..."
        self.export_button.update()
        
        # 在后台线程中执行导出操作
        threading.Thread(target=self.export_data_thread, daemon=True).start()
    
    def export_data_thread(self):
        """在后台线程中执行数据导出"""
        try:
            self.log_message("开始准备导出数据...")
            
            # 格式化日期为SQL查询格式
            start_date_str = self.start_date.strftime("%Y-%m-%d")
            end_date_str = (self.end_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # 包含结束日期
            
            self.log_message(f"查询时间范围: {start_date_str} 至 {end_date_str}")
            
            # 构建SQL查询
            query = f"""SELECT id, agent_id, agent_name, advertiser_id, advertiser_name, 
                first_industry, second_industry, account_source, company_name, 
                audit_pass_time, account_status, register_time, cost, cash_cost, 
                bid_cost, brand_cost, grants_cost, cpc_cost, cpm_cost, ocpc_cost, 
                cpa_cost, ocpm_cost, cpv_cost, cpt_cost, gd_cost, `show`, cpm, 
                click, ctr, cpc, transfer_count, today_cost, transfer_amount, 
                history_cost, register_days, first_cost_time, cash_balance, 
                rant_balance, year, month, day, date, is_sync, native_province_cost, 
                out_province_cost, out_province_ids, is_sync_native, first_recharge_amount, 
                first_recharge_time, last_renew_time, total_renew_number, total_balance, 
                valid_balance, is_sycn_actual, saler_user_id, saler_user_name, 
                saler_dept_id, saler_dept_name, oper_user_id, oper_user_name, 
                oper_dept_id, oper_dept_name, create_time, create_user, update_time, 
                update_user, remark, del_flag 
                FROM dsp_advertiser_cost 
                WHERE create_time >= '{start_date_str}' AND create_time < '{end_date_str}'"""
            
            # 连接数据库并执行查询
            self.log_message("连接数据库...")
            conn = mysql.connector.connect(**self.db_config)
            
            try:
                cursor = conn.cursor(dictionary=True)
                self.log_message("执行数据查询...")
                cursor.execute(query)
                
                # 获取查询结果
                results = cursor.fetchall()
                row_count = len(results)
                self.log_message(f"查询完成，共获取 {row_count} 条记录")
                
                if row_count == 0:
                    self.log_message("未找到符合条件的数据")
                    return
                
                # 生成CSV文件名
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f"消耗数据_{start_date_str}_{self.end_date.strftime('%Y-%m-%d')}_{timestamp}.csv"
                filepath = os.path.join(self.export_dir, filename)
                
                # 使用pandas导出为CSV
                self.log_message(f"开始导出数据到CSV文件...")
                df = pd.DataFrame(results)
                df.to_csv(filepath, index=False, encoding='utf-8-sig')  # 使用带BOM的UTF-8编码以支持Excel正确显示中文
                
                self.log_message(f"导出成功! 文件保存在: {filepath}")
                
                # 打开文件所在目录
                os.startfile(self.export_dir)
                
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
                    self.log_message("数据库连接已关闭")
        
        except Exception as e:
            self.log_message(f"导出过程中发生错误: {str(e)}")
        
        finally:
            # 重置UI状态
            self.is_exporting = False
            self.export_button.disabled = False
            self.export_button.text = "开始导出"
            self.export_button.update()


def main(page: ft.Page):
    print("应用程序启动中...")
    app = DataExportApp()
    print("构建用户界面...")
    app.build_ui(page)
    print("应用程序已启动!")


if __name__ == "__main__":
    ft.app(target=main)