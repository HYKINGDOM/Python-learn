# PDF转Markdown工具

这是一个基于Python的工具，用于将PDF文件转换为Markdown格式，同时保留原文件的样式和格式。该工具提供了一个HTTP接口，可以上传PDF文件并获取转换后的Markdown文件和提取的图片。

## 功能特点

- 将PDF文件转换为Markdown格式
- 保持原文件的样式和格式
- 提取PDF中的图片并插入到Markdown中
- 自动过滤PDF中的水印（包括表格中的水印）
- 智能识别和转换表格（包括表格图片）
- 提供HTTP接口，转换完成后以ZIP文件形式返回结果

## 环境要求

- Python 3.12.8 或更高版本
- Windows 11 操作系统

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 启动服务

```bash
python app.py
```

服务将在 http://localhost:5000 上运行。

### 通过Web界面使用

1. 打开浏览器访问 http://localhost:5000
2. 上传PDF文件
3. 点击"转换"按钮
4. 下载转换后的ZIP文件，其中包含Markdown文件和提取的图片

### 通过API使用

可以通过HTTP POST请求直接调用API：

```bash
curl -X POST -F "file=@your_file.pdf" http://localhost:5000/convert -o result.zip
```

或者使用Python requests库：

```python
import requests

url = "http://localhost:5000/convert"
files = {"file": open("your_file.pdf", "rb")}
response = requests.post(url, files=files)

with open("result.zip", "wb") as f:
    f.write(response.content)
```

## 项目结构

```
.
├── app.py              # 主应用文件，包含Flask服务和PDF转换逻辑
├── requirements.txt    # 项目依赖
├── uploads/            # 上传的PDF文件存储目录
└── outputs/            # 转换后的Markdown和图片输出目录
```

## 技术实现

- 使用Flask框架提供HTTP服务
- 使用PyMuPDF (fitz)库处理PDF文件、提取图片和移除水印
- 使用pymupdf4llm库将PDF转换为Markdown格式
- 增强表格识别和处理功能，确保表格被正确转换
- 实现表格中水印的检测和移除
- 支持将表格区域渲染为图片，确保复杂表格的正确显示
- 使用Python标准库处理文件操作和压缩

## 注意事项

- 上传文件大小限制为16MB
- 仅支持PDF文件格式
- 水印移除功能可能不适用于所有类型的水印，但已优化对表格中水印的处理
- 复杂的PDF布局可能会影响转换质量
- 表格处理支持两种模式：Markdown表格格式和表格图片格式，对于复杂表格会自动选择图片模式
- 对于无法正确识别为Markdown表格的内容，系统会自动将其作为图片提取