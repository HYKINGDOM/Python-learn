import os
import platform
from PIL import Image, ImageDraw, ImageFont


def create_app_icon():
    """创建应用图标"""
    print("开始创建应用图标...")
    
    # 创建一个512x512的图像（推荐的图标大小）
    img_size = 512
    img = Image.new('RGBA', (img_size, img_size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景
    circle_radius = img_size // 2 - 10
    circle_center = (img_size // 2, img_size // 2)
    draw.ellipse(
        [(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
         (circle_center[0] + circle_radius, circle_center[1] + circle_radius)],
        fill=(65, 105, 225, 255)  # 蓝色背景
    )
    
    # 尝试加载字体，如果失败则使用默认字体
    try:
        # 尝试使用系统字体
        if platform.system() == "Windows":
            font_path = "C:\\Windows\\Fonts\\simhei.ttf"  # 黑体
        elif platform.system() == "Darwin":  # macOS
            font_path = "/System/Library/Fonts/PingFang.ttc"
        else:  # Linux或其他
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            
        if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, size=img_size // 3)
        else:
            # 如果找不到指定字体，使用默认字体
            font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
    
    # 绘制文本
    text = "导出"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_position = (
        (img_size - text_width) // 2,
        (img_size - text_height) // 2
    )
    
    draw.text(
        text_position,
        text,
        font=font,
        fill=(255, 255, 255, 255)  # 白色文字
    )
    
    # 保存为不同格式的图标
    if platform.system() == "Windows":
        # 保存为ICO格式（Windows）
        img.save("app_icon.ico", format="ICO")
        print("已创建Windows图标: app_icon.ico")
    elif platform.system() == "Darwin":  # macOS
        # 保存为PNG格式，后续可以转换为ICNS（macOS）
        img.save("app_icon.png", format="PNG")
        print("已创建PNG图标: app_icon.png")
        print("注意: 要创建macOS的.icns文件，请使用iconutil工具转换")
    else:
        # 保存为PNG格式（通用）
        img.save("app_icon.png", format="PNG")
        print("已创建PNG图标: app_icon.png")


if __name__ == "__main__":
    try:
        # 检查是否已安装Pillow
        import PIL
        create_app_icon()
    except ImportError:
        print("错误: 未安装Pillow库，请先安装: pip install Pillow")
    except Exception as e:
        print(f"创建图标时发生错误: {e}")