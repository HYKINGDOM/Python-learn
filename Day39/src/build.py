import os
import platform
import subprocess


def build_executable():
    """根据当前操作系统构建可执行文件"""
    print("开始构建可执行文件...")
    
    # 获取当前操作系统
    system = platform.system()
    
    # 构建命令
    if system == "Windows":
        print("检测到Windows系统，构建.exe文件...")
        cmd = [
            "pyinstaller",
            "--name=消耗数据导出工具",
            "--windowed",
            "--onefile",
            "--clean",
            "--icon=app_icon.ico",  # 如果有图标文件，请确保存在
            "data_export_app.py"
        ]
    elif system == "Darwin":  # macOS
        print("检测到macOS系统，构建.dmg文件...")
        cmd = [
            "pyinstaller",
            "--name=消耗数据导出工具",
            "--windowed",
            "--onefile",
            "--clean",
            "--icon=app_icon.icns",  # 如果有图标文件，请确保存在
            "data_export_app.py"
        ]
    else:
        print(f"不支持的操作系统: {system}")
        return
    
    # 执行构建命令
    try:
        subprocess.run(cmd, check=True)
        
        # 构建成功后的输出路径
        dist_path = os.path.abspath("dist")
        print(f"构建成功! 可执行文件位于: {dist_path}")
        
        # 自动打开输出目录
        if system == "Windows":
            os.startfile(dist_path)
        elif system == "Darwin":
            subprocess.run(["open", dist_path])
            
    except subprocess.CalledProcessError as e:
        print(f"构建失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    # 确保在脚本所在目录执行
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 检查是否已安装依赖
    print("检查依赖项...")
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("依赖项安装完成")
    except Exception as e:
        print(f"依赖项安装失败: {e}")
        exit(1)
    
    # 构建可执行文件
    build_executable()