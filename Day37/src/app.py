import os
import tempfile
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import pymupdf4llm
import fitz  # PyMuPDF
import shutil
from pathlib import Path

app = Flask(__name__)

# 配置上传文件夹
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
OUTPUT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
ALLOWED_EXTENSIONS = {'pdf'}

# 确保上传和输出文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为16MB


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def remove_watermark(pdf_path, output_path):
    """移除PDF中的水印
    
    使用PyMuPDF (fitz)库移除PDF中的水印，包括表格中的水印。这个函数尝试识别和移除常见的水印元素。
    
    Args:
        pdf_path: 输入PDF文件路径
        output_path: 输出PDF文件路径
    
    Returns:
        bool: 是否成功移除水印
    """
    try:
        # 打开PDF文件
        doc = fitz.open(pdf_path)
        
        # 遍历每一页
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # 获取页面上的所有对象
            page_dict = page.get_text("dict")
            artifacts = page_dict["blocks"]
            
            # 水印特征 - 通常是重复出现的文本，位于页面中央或角落，透明度高
            watermark_candidates = []
            
            # 查找可能的水印
            for artifact in artifacts:
                # 检查文本块
                if artifact.get("type") == 0:  # 文本块
                    lines = artifact.get("lines", [])
                    for line in lines:
                        spans = line.get("spans", [])
                        for span in spans:
                            text = span.get("text", "").strip()
                            font_size = span.get("size", 0)
                            color = span.get("color", 0)
                            
                            # 水印特征：文本较短，字体较大或较小，颜色较浅
                            if (text and 
                                (len(text) < 30 or text.count(" ") > len(text) / 3) and
                                (font_size > 14 or font_size < 6 or 
                                 (isinstance(color, int) and color > 0x999999))):
                                watermark_candidates.append((text, span))
                
                # 检查图像块（可能包含水印）
                elif artifact.get("type") == 1:  # 图像块
                    # 处理可能包含水印的图像
                    pass
            
            # 检测重复出现的文本（可能是水印）
            text_counts = {}
            for text, _ in watermark_candidates:
                text_counts[text] = text_counts.get(text, 0) + 1
            
            # 如果某个文本在页面上重复出现多次，很可能是水印
            watermarks = [text for text, count in text_counts.items() if count > 1]
            
            # 应用redactions移除水印
            if watermarks:
                for text in watermarks:
                    instances = page.search_for(text)
                    for inst in instances:
                        page.add_redact_annot(inst, fill=(1, 1, 1))
                    page.apply_redactions()
            
            # 处理表格中的水印
            # 表格通常是类型为4的块
            for artifact in artifacts:
                if artifact.get("type") == 4:  # 表格或背景
                    # 清理表格内容，移除可能的水印
                    page.clean_contents()
            
            # 标准化页面内容
            page.clean_contents()
        
        # 保存修改后的文件
        doc.save(output_path)
        doc.close()
        return True
    except Exception as e:
        print(f"移除水印时出错: {e}")
        return False


def pdf_to_markdown(pdf_path, output_dir, filename, extract_tables_as_images=None, verbose=False):
    """将PDF转换为Markdown
    
    使用pymupdf4llm库将PDF转换为Markdown格式，并保存图片。
    增强了表格识别和处理功能，确保表格被正确转换为Markdown格式。
    
    Args:
        pdf_path: PDF文件路径
        output_dir: 输出目录
        filename: 文件名（不含扩展名）
        extract_tables_as_images: 是否将表格作为图片提取
            - True: 将表格作为图片提取
            - False: 将表格转换为Markdown格式
            - None: 自动决定（默认）
        verbose: 是否显示详细处理信息
    
    Returns:
        tuple: (markdown文件路径, 是否成功)
    """
    try:
        # 创建输出目录
        md_output_dir = os.path.join(output_dir, filename)
        os.makedirs(md_output_dir, exist_ok=True)
        
        if verbose:
            print(f"处理PDF文件: {pdf_path}")
            print(f"输出目录: {md_output_dir}")
            if extract_tables_as_images is True:
                print("表格处理模式: 图片模式")
            elif extract_tables_as_images is False:
                print("表格处理模式: Markdown模式")
            else:
                print("表格处理模式: 自动模式")
        
        # 转换PDF为Markdown，设置高级选项以增强表格识别
        md_text = pymupdf4llm.to_markdown(
            pdf_path,
            # 增强表格识别和处理的选项
            detect_tables=True,           # 启用表格检测
            detect_vertical_lines=True,   # 检测垂直线（表格边界）
            detect_horizontal_lines=True, # 检测水平线（表格边界）
            preserve_images=True,         # 保留图片
            extract_tables_as_images=extract_tables_as_images # 表格处理模式
        )
        
        # 处理表格中可能的水印文本
        # 查找Markdown表格标记并清理其中可能的水印
        lines = md_text.split('\n')
        cleaned_lines = []
        in_table = False
        
        for line in lines:
            # 检测表格开始和结束
            if line.strip().startswith('|') and line.strip().endswith('|'):
                in_table = True
                # 清理表格行中可能的水印
                cells = line.split('|')
                cleaned_cells = []
                
                for cell in cells:
                    cell_text = cell.strip()
                    # 如果单元格文本看起来像水印（短文本，重复出现等），则清理
                    if len(cell_text) < 10 and cell_text.upper() == cell_text and cell_text:
                        cleaned_cells.append('')  # 移除可能的水印
                    else:
                        cleaned_cells.append(cell)
                
                cleaned_line = '|'.join(cleaned_cells)
                cleaned_lines.append(cleaned_line)
            else:
                if in_table and line.strip() == '':
                    in_table = False
                cleaned_lines.append(line)
        
        md_text = '\n'.join(cleaned_lines)
        
        # 保存Markdown文件
        md_file_path = os.path.join(md_output_dir, f"{filename}.md")
        Path(md_file_path).write_text(md_text, encoding="utf-8")
        
        # 提取图片，包括可能的表格图片
        doc = fitz.open(pdf_path)
        img_count = 0
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # 提取常规图片
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]  # 图片的xref
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # 保存图片
                img_filename = f"image_{page_num+1}_{img_index+1}.{base_image['ext']}"
                img_path = os.path.join(md_output_dir, img_filename)
                
                with open(img_path, "wb") as img_file:
                    img_file.write(image_bytes)
                
                img_count += 1
            
            # 检测并提取表格图片
            # 获取页面上的所有对象
            page_dict = page.get_text("dict")
            blocks = page_dict["blocks"]
            
            # 查找表格块
            table_count = 0
            for block_idx, block in enumerate(blocks):
                # 表格通常是类型为4的块
                if block.get("type") == 4:  # 表格
                    table_count += 1
                    if verbose:
                        print(f"在页面 {page_num+1} 上检测到表格 #{table_count}")
                    
                    # 将表格区域渲染为图片
                    table_rect = fitz.Rect(block.get("bbox"))
                    # 使用更高分辨率以确保表格清晰
                    table_pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=table_rect)
                    
                    # 保存表格图片
                    table_img_filename = f"table_{page_num+1}_{block_idx+1}.png"
                    table_img_path = os.path.join(md_output_dir, table_img_filename)
                    table_pixmap.save(table_img_path)
                    
                    if verbose:
                        print(f"  - 已保存表格图片: {table_img_filename}")
                    
                    # 在Markdown中添加表格图片引用
                    # 尝试多种模式匹配表格的开始部分
                    table_patterns = [
                        f"\n\n|" + f"\n|"*3,  # 标准表格格式
                        f"\n|" + f"\n|"*2,    # 紧凑表格格式
                        f"\n\n\|" + f"[^\n]*\n\|"*2  # 复杂表格格式
                    ]
                    
                    table_img_ref = f"\n\n![表格 {page_num+1}-{block_idx+1}]({table_img_filename})\n\n"
                    
                    # 尝试替换表格
                    replaced = False
                    for pattern in table_patterns:
                        if pattern in md_text:
                            md_text = md_text.replace(pattern, table_img_ref, 1)
                            replaced = True
                            break
                    
                    # 如果没有找到匹配的表格模式，尝试在文档末尾添加
                    if not replaced:
                        md_text += f"\n\n## 附加表格 {page_num+1}-{block_idx+1}\n" + table_img_ref
                        if verbose:
                            print(f"  - 未找到匹配的表格文本，已将表格图片添加到文档末尾")
                    
                    img_count += 1
        
        # 如果有表格图片添加，重新保存Markdown文件
        Path(md_file_path).write_text(md_text, encoding="utf-8")
        
        doc.close()
        
        # 创建一个压缩文件
        zip_path = os.path.join(output_dir, f"{filename}.zip")
        shutil.make_archive(zip_path[:-4], 'zip', md_output_dir)
        
        return zip_path, True
    except Exception as e:
        print(f"PDF转Markdown时出错: {e}")
        return None, False


@app.route('/convert', methods=['POST'])
def convert_pdf_to_markdown():
    """PDF转Markdown的HTTP接口
    
    接收上传的PDF文件，移除水印，转换为Markdown，并返回包含Markdown和图片的zip文件。
    
    支持的参数:
        - file: PDF文件
        - remove_watermark: 是否移除水印 (1或0，默认为1)
        - table_mode: 表格处理模式 (markdown, image, auto，默认为auto)
        - verbose: 是否显示详细信息 (1或0，默认为0)
    
    Returns:
        Flask Response: 包含转换结果的响应
    """
    # 检查是否有文件上传
    if 'file' not in request.files:
        return jsonify({
            'error': '没有上传文件'
        }), 400
    
    file = request.files['file']
    
    # 检查文件名是否为空
    if file.filename == '':
        return jsonify({
            'error': '未选择文件'
        }), 400
    
    # 获取其他参数
    remove_watermark = request.form.get('remove_watermark', '1') == '1'
    table_mode = request.form.get('table_mode', 'auto')
    verbose = request.form.get('verbose', '0') == '1'
    
    # 验证表格模式参数
    if table_mode not in ['markdown', 'image', 'auto']:
        table_mode = 'auto'
    
    # 设置表格处理选项
    if table_mode == 'markdown':
        extract_tables_as_images = False
    elif table_mode == 'image':
        extract_tables_as_images = True
    else:  # auto
        extract_tables_as_images = None
    
    # 检查文件类型
    if not allowed_file(file.filename):
        return jsonify({
            'error': '不支持的文件类型，仅支持PDF文件'
        }), 400
    
    try:
        # 保存上传的文件
        filename = secure_filename(file.filename)
        base_filename = os.path.splitext(filename)[0]
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)
        
        # 创建临时文件用于存储无水印的PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
            no_watermark_path = temp_file.name
        
        # 根据参数决定是否移除水印
        if remove_watermark:
            remove_watermark_success = remove_watermark(pdf_path, no_watermark_path)
            pdf_to_convert = no_watermark_path if remove_watermark_success else pdf_path
        else:
            pdf_to_convert = pdf_path
            remove_watermark_success = False
        
        # 转换为Markdown，传递表格处理选项
        zip_path, convert_success = pdf_to_markdown(
            pdf_to_convert,
            app.config['OUTPUT_FOLDER'],
            base_filename,
            extract_tables_as_images=extract_tables_as_images,
            verbose=verbose
        )
        
        if not convert_success:
            return jsonify({
                'error': 'PDF转换失败'
            }), 500
        
        # 返回zip文件
        return send_file(
            zip_path,
            as_attachment=True,
            download_name=f"{base_filename}.zip",
            mimetype='application/zip'
        )
    
    except Exception as e:
        return jsonify({
            'error': f'处理文件时出错: {str(e)}'
        }), 500
    finally:
        # 清理临时文件
        if 'no_watermark_path' in locals() and os.path.exists(no_watermark_path):
            os.unlink(no_watermark_path)


@app.route('/', methods=['GET'])
def index():
    """首页，显示上传表单"""
    return '''
    <!doctype html>
    <html>
    <head>
        <title>PDF转Markdown工具</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .container {
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            .form-group {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            input[type="file"] {
                width: 100%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #45a049;
            }
            button:disabled {
                background-color: #cccccc;
                cursor: not-allowed;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            .features {
                margin-top: 30px;
            }
            .features h2 {
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }
            .features ul {
                padding-left: 20px;
            }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.getElementById('convert-form');
                const fileInput = document.getElementById('file');
                const fileError = document.getElementById('file-error');
                const fileLabel = document.getElementById('file-label');
                const serverError = document.getElementById('server-error');
                const successMessage = document.getElementById('success-message');
                const submitBtn = document.getElementById('submit-btn');
                const loading = document.getElementById('loading');
                const progressBar = document.getElementById('progress-bar');
                
                // 初始状态下禁用提交按钮
                submitBtn.disabled = true;
                
                // 重置表单状态
                function resetForm() {
                    loading.style.display = 'none';
                    submitBtn.disabled = false;
                    submitBtn.textContent = '转换';
                    // 清空文件输入框
                    form.reset();
                    // 隐藏文件名标签
                    fileLabel.style.display = 'none';
                    // 重置进度条
                    progressBar.style.width = '0%';
                    progressBar.textContent = '0%';
                    // 3秒后隐藏成功消息
                    setTimeout(function() {
                        successMessage.style.display = 'none';
                    }, 3000);
                }
                
                // 显示服务器错误
                function showServerError(message) {
                    serverError.textContent = message || '处理请求时出错，请重试';
                    serverError.style.display = 'block';
                    resetForm();
                }
                
                form.addEventListener('submit', function(event) {
                    event.preventDefault(); // 阻止表单默认提交
                    
                    if (!fileInput.files || fileInput.files.length === 0) {
                        fileError.style.display = 'block';
                        return;
                    }
                    
                    // 隐藏错误和成功信息
                    fileError.style.display = 'none';
                    serverError.style.display = 'none';
                    successMessage.style.display = 'none';
                    
                    // 显示加载状态并禁用按钮
                    loading.style.display = 'block';
                    submitBtn.disabled = true;
                    submitBtn.textContent = '处理中...';
                    
                    // 创建FormData对象
                    const formData = new FormData(form);
                    
                    // 使用XMLHttpRequest代替fetch以支持进度监控
                    const xhr = new XMLHttpRequest();
                    
                    // 监听上传进度
                    xhr.upload.addEventListener('progress', function(event) {
                        if (event.lengthComputable) {
                            const percentComplete = Math.round((event.loaded / event.total) * 100);
                            progressBar.style.width = percentComplete + '%';
                            progressBar.textContent = percentComplete + '%';
                        }
                    });
                    
                    // 监听请求完成
                    xhr.addEventListener('load', function() {
                        // 上传完成后，将进度条设置为100%
                        progressBar.style.width = '100%';
                        progressBar.textContent = '100%';
                        
                        const response = xhr;
                        if (response.status >= 200 && response.status < 300) {
                            // 检查响应类型
                            const contentType = response.getResponseHeader('content-type');
                            if (contentType && contentType.includes('application/json')) {
                                // 如果是JSON响应，说明有错误
                                try {
                                    const data = JSON.parse(response.responseText);
                                    throw new Error(data.error || '处理请求时出错');
                                } catch (error) {
                                    console.error('Error:', error);
                                    showServerError(error.message);
                                }
                            } else {
                                // 如果是文件响应，触发下载
                                const contentDisposition = response.getResponseHeader('content-disposition');
                                const filename = contentDisposition
                                    ? contentDisposition.split('filename=')[1].replace(/"/g, '')
                                    : 'output.zip';
                                
                                const blob = new Blob([response.response], { type: response.getResponseHeader('content-type') });
                                const url = window.URL.createObjectURL(blob);
                                const a = document.createElement('a');
                                a.style.display = 'none';
                                a.href = url;
                                a.download = filename;
                                document.body.appendChild(a);
                                a.click();
                                window.URL.revokeObjectURL(url);
                                // 显示成功消息
                                successMessage.style.display = 'block';
                                resetForm();
                            }
                        } else {
                            // 处理HTTP错误
                            try {
                                const data = JSON.parse(response.responseText);
                                throw new Error(data.error || `服务器返回错误: ${response.status}`);
                            } catch (error) {
                                console.error('Error:', error);
                                showServerError(error.message);
                            }
                        }
                    });
                    
                    // 监听请求错误
                    xhr.addEventListener('error', function() {
                        console.error('Request failed');
                        showServerError('网络错误，请检查您的网络连接');
                    });
                    
                    // 监听请求中止
                    xhr.addEventListener('abort', function() {
                        console.error('Request aborted');
                        showServerError('请求被中止');
                    });
                    
                    // 打开请求
                    xhr.open('POST', '/convert');
                    xhr.responseType = 'blob';
                    
                    // 发送请求
                    xhr.send(formData);
                });
                
                fileInput.addEventListener('change', function() {
                    if (fileInput.files && fileInput.files.length > 0) {
                        fileError.style.display = 'none';
                        submitBtn.disabled = false; // 有文件时启用按钮
                        
                        // 检查文件类型和大小
                        const file = fileInput.files[0];
                        const fileName = file.name;
                        const fileExt = fileName.split('.').pop().toLowerCase();
                        const fileSize = file.size; // 文件大小（字节）
                        const maxSize = 16 * 1024 * 1024; // 16MB
                        
                        // 显示文件名
                        fileLabel.textContent = fileName;
                        fileLabel.style.display = 'inline-block';
                        fileLabel.title = fileName; // 添加工具提示，显示完整文件名
                        
                        if (fileExt !== 'pdf') {
                            fileError.textContent = '请选择PDF文件';
                            fileError.style.display = 'block';
                            submitBtn.disabled = true;
                        } else if (fileSize > maxSize) {
                            fileError.textContent = `文件大小超过限制（最大16MB），当前大小：${(fileSize / (1024 * 1024)).toFixed(2)}MB`;
                            fileError.style.display = 'block';
                            submitBtn.disabled = true;
                        }
                    } else {
                        submitBtn.disabled = true; // 无文件时禁用按钮
                        fileLabel.style.display = 'none'; // 隐藏文件名标签
                    }
                });
            });
        </script>
    </head>
    <body>
        <h1>PDF转Markdown工具</h1>
        <div class="container">
            <form action="/convert" method="post" enctype="multipart/form-data" id="convert-form">
                <div id="server-error" style="display: none; color: red; margin-bottom: 15px; padding: 10px; background-color: #ffeeee; border: 1px solid #ffcccc; border-radius: 4px;"></div>
                <div id="success-message" style="display: none; color: green; margin-bottom: 15px; padding: 10px; background-color: #eeffee; border: 1px solid #ccffcc; border-radius: 4px;">转换成功！文件已开始下载。</div>
                <div class="form-group">
                    <label for="file">选择PDF文件:</label>
                    <div style="display: flex; align-items: center;">
                        <input type="file" name="file" id="file" accept=".pdf" required style="flex: 1;">
                        <label id="file-label" style="margin-left: 10px; display: none; background: #f0f0f0; padding: 5px 10px; border-radius: 4px; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"></label>
                    </div>
                    <div id="file-error" style="color: red; display: none; margin-top: 5px;">请选择一个PDF文件</div>
                </div>
                
                <div class="form-group">
                    <label>表格处理模式:</label>
                    <div style="margin-top: 5px;">
                        <label style="display: inline; font-weight: normal;">
                            <input type="radio" name="table_mode" value="auto" checked> 自动选择
                        </label>
                        <label style="display: inline; font-weight: normal; margin-left: 15px;">
                            <input type="radio" name="table_mode" value="markdown"> Markdown表格
                        </label>
                        <label style="display: inline; font-weight: normal; margin-left: 15px;">
                            <input type="radio" name="table_mode" value="image"> 表格图片
                        </label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label style="display: inline; font-weight: normal;">
                        <input type="checkbox" name="remove_watermark" value="1" checked> 移除水印
                    </label>
                </div>
                
                <div class="form-group">
                    <label style="display: inline; font-weight: normal;">
                        <input type="checkbox" name="verbose" value="1"> 显示详细处理信息
                    </label>
                </div>
                
                <button type="submit" id="submit-btn">转换</button>
                <div id="loading" style="display: none; margin-top: 10px; text-align: center;">
                    <div style="display: inline-block; width: 20px; height: 20px; border: 3px solid rgba(0,0,0,.3); border-radius: 50%; border-top-color: #4CAF50; animation: spin 1s ease-in-out infinite;"></div>
                    <span style="margin-left: 10px;">正在处理，请稍候...</span>
                    <div style="margin-top: 10px; width: 100%; background-color: #f1f1f1; border-radius: 4px; overflow: hidden;">
                        <div id="progress-bar" style="width: 0%; height: 20px; background-color: #4CAF50; text-align: center; line-height: 20px; color: white;">0%</div>
                    </div>
                </div>
            </form>
        </div>
        
        <div class="features">
            <h2>功能特点</h2>
            <ul>
                <li>将PDF文件转换为Markdown格式</li>
                <li>保持原文件的样式和格式</li>
                <li>提取PDF中的图片并插入到Markdown中</li>
                <li>智能识别和转换表格（支持Markdown表格和表格图片）</li>
                <li>自动过滤PDF中的水印（包括表格中的水印）</li>
                <li>支持多种表格处理模式（自动、Markdown、图片）</li>
                <li>返回包含Markdown和图片的压缩包</li>
            </ul>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)