# Chrome Bookmarks Tool

这是一个用于分析和清理Chrome书签的Python工具。它可以检测无效的书签链接并查找重复的书签。

## 功能特性

- **跨平台支持**：自动检测Windows、macOS和Linux系统的Chrome书签路径
- **书签解析**：从Chrome的Bookmarks文件中提取所有书签信息
- **链接检查**：使用多线程快速验证书签链接的有效性
- **重复检测**：识别具有相同URL的重复书签
- **安全清理**：提供选项清理重复书签（当前代码中该功能被注释掉，需要手动启用）

## 主要模块

- [get_chrome_bookmark_path()](file://D:\project\github\Python-learn\Day36\src\chrome_bookmark.py#L10-L29)：获取当前系统Chrome书签文件的路径
- [read_chrome_bookmarks()](file://D:\project\github\Python-learn\Day36\src\chrome_bookmark.py#L58-L72)：读取并解析Chrome书签文件
- [check_url_validity()](file://D:\project\github\Python-learn\Day36\src\chrome_bookmark.py#L75-L94)：验证单个书签链接的可访问性
- [find_duplicate_bookmarks()](file://D:\project\github\Python-learn\Day36\src\chrome_bookmark.py#L97-L114)：查找重复的书签
- [clean_duplicate_bookmarks()](file://D:\project\github\Python-learn\Day36\src\chrome_bookmark.py#L117-L131)：清理重复的书签，保留第一个出现的

## 使用方法

1. 克隆仓库到本地
2. 安装依赖：`pip install requests`
3. 运行程序：`python chrome_bookmark.py`

程序将输出：
- 读取的书签总数
- 检测到的无效链接及其原因
- 发现的重复书签组
- 提供清理重复书签的交互式选项

## 注意事项

- 程序不会直接修改原始书签文件，清理功能当前被注释掉，如需启用请取消相关代码的注释
- 更新书签文件前会自动创建备份
- 建议在正式使用前测试代码以确保符合您的需求

## 依赖库

- `requests`：用于网络请求验证
- `concurrent.futures`：实现多线程链接检查

这个工具可以作为Chrome书签管理的基础框架，您可以根据需要扩展更多功能，如导出为特定格式、定期检查任务等。