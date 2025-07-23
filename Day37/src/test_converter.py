import os
import sys
import argparse
from pathlib import Path

# 确保可以导入app.py中的函数
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app import remove_watermark, pdf_to_markdown

def main():
    """测试PDF转Markdown功能
    
    用法:
        python test_converter.py --pdf_path path/to/your/file.pdf
    """
    parser = argparse.ArgumentParser(description='测试PDF转Markdown功能')
    parser.add_argument('--pdf_path', required=True, help='PDF文件路径')
    parser.add_argument('--output_dir', default='test_output', help='输出目录')
    parser.add_argument('--remove_watermark', action='store_true', help='是否移除水印')
    parser.add_argument('--table_mode', choices=['markdown', 'image', 'auto'], default='auto', 
                        help='表格处理模式：markdown(纯文本表格)、image(表格图片)或auto(自动选择)')
    parser.add_argument('--verbose', action='store_true', help='显示详细处理信息')
    
    args = parser.parse_args()
    
    # 确保输出目录存在
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取文件名（不含扩展名）
    base_filename = os.path.splitext(os.path.basename(args.pdf_path))[0]
    
    # 如果需要移除水印
    if args.remove_watermark:
        print(f"正在移除水印...")
        no_watermark_path = os.path.join(output_dir, f"{base_filename}_no_watermark.pdf")
        success = remove_watermark(args.pdf_path, no_watermark_path)
        
        if success:
            print(f"水印移除成功，保存到: {no_watermark_path}")
            pdf_path = no_watermark_path
        else:
            print(f"水印移除失败，将使用原始PDF")
            pdf_path = args.pdf_path
    else:
        pdf_path = args.pdf_path
    
    # 转换为Markdown
    print(f"正在将PDF转换为Markdown...")
    
    # 根据表格模式设置参数
    table_mode = args.table_mode
    if table_mode == 'markdown':
        print("使用Markdown表格模式 - 表格将转换为Markdown格式")
        extract_tables_as_images = False
    elif table_mode == 'image':
        print("使用图片表格模式 - 表格将转换为图片")
        extract_tables_as_images = True
    else:  # auto
        print("使用自动表格模式 - 系统将自动选择最佳表示方式")
        extract_tables_as_images = None  # 让函数自动决定
    
    # 添加详细日志选项
    verbose = args.verbose
    if verbose:
        print("启用详细日志输出")
    
    # 调用转换函数，传递额外参数
    zip_path, success = pdf_to_markdown(
        pdf_path, 
        output_dir, 
        base_filename,
        extract_tables_as_images=extract_tables_as_images,
        verbose=verbose
    )
    
    if success:
        print(f"转换成功，结果保存到: {zip_path}")
        print("\n提示: 解压ZIP文件后，可以查看转换后的Markdown文件和提取的图片")
    else:
        print(f"转换失败")

if __name__ == '__main__':
    main()