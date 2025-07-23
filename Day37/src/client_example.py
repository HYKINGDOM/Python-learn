import requests
import argparse
import os

def convert_pdf_to_markdown(pdf_path, server_url="http://localhost:5000/convert", output_path=None, 
                       table_mode="auto", remove_watermark=True, verbose=False):
    """通过API调用将PDF转换为Markdown
    
    Args:
        pdf_path: PDF文件路径
        server_url: 服务器URL
        output_path: 输出文件路径，默认为当前目录下的[filename].zip
        table_mode: 表格处理模式，可选值为"auto"、"markdown"或"image"
        remove_watermark: 是否移除水印
        verbose: 是否显示详细处理信息
    
    Returns:
        bool: 是否成功
    """
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 文件 {pdf_path} 不存在")
        return False
    
    # 设置默认输出路径
    if output_path is None:
        base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = f"{base_filename}.zip"
    
    try:
        print(f"正在上传文件 {pdf_path} 到服务器...")
        
        # 准备文件和参数
        with open(pdf_path, "rb") as f:
            files = {"file": (os.path.basename(pdf_path), f, "application/pdf")}
            
            # 准备表单数据
            data = {
                "table_mode": table_mode,
                "remove_watermark": "1" if remove_watermark else "0",
                "verbose": "1" if verbose else "0"
            }
            
            print(f"使用参数: 表格模式={table_mode}, 移除水印={remove_watermark}, 详细信息={verbose}")
            
            # 发送请求
            response = requests.post(server_url, files=files, data=data)
        
        # 检查响应
        if response.status_code == 200:
            # 保存结果
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            print(f"转换成功，结果保存到: {output_path}")
            return True
        else:
            print(f"转换失败，服务器返回状态码: {response.status_code}")
            if response.headers.get('Content-Type') == 'application/json':
                print(f"错误信息: {response.json()}")
            return False
    
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return False

def main():
    """命令行入口
    
    用法:
        python client_example.py --pdf_path path/to/your/file.pdf [--server_url http://localhost:5000/convert] [--output_path result.zip]
        [--table_mode auto|markdown|image] [--no_watermark_removal] [--verbose]
    """
    parser = argparse.ArgumentParser(description='PDF转Markdown客户端示例')
    parser.add_argument('--pdf_path', required=True, help='PDF文件路径')
    parser.add_argument('--server_url', default="http://localhost:5000/convert", help='服务器URL')
    parser.add_argument('--output_path', help='输出文件路径')
    parser.add_argument('--table_mode', choices=['auto', 'markdown', 'image'], default='auto',
                        help='表格处理模式：auto(自动选择)、markdown(纯文本表格)或image(表格图片)')
    parser.add_argument('--no_watermark_removal', action='store_true', 
                        help='不移除水印（默认会移除）')
    parser.add_argument('--verbose', action='store_true', 
                        help='显示详细处理信息')
    
    args = parser.parse_args()
    
    convert_pdf_to_markdown(
        pdf_path=args.pdf_path, 
        server_url=args.server_url, 
        output_path=args.output_path,
        table_mode=args.table_mode,
        remove_watermark=not args.no_watermark_removal,
        verbose=args.verbose
    )

if __name__ == '__main__':
    main()