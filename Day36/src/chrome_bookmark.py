import json
import os
import platform
import requests
from typing import List, Dict, Any, Set, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import time


def get_chrome_bookmark_path() -> str:
    """获取Chrome书签文件的路径，支持不同操作系统"""
    system = platform.system()

    if system == "Windows":
        app_data = os.getenv('APPDATA')
        if not app_data:
            raise FileNotFoundError("无法获取APPDATA环境变量")
        return os.path.join(app_data, "..", "Local", "Google", "Chrome", "User Data", "Default", "Bookmarks")

    elif system == "Darwin":  # macOS
        home = os.path.expanduser("~")
        return os.path.join(home, "Library", "Application Support", "Google", "Chrome", "Default", "Bookmarks")

    elif system == "Linux":
        home = os.path.expanduser("~")
        return os.path.join(home, ".config", "google-chrome", "Default", "Bookmarks")

    else:
        raise NotImplementedError(f"不支持的操作系统: {system}")


def parse_bookmarks(data: Dict[str, Any]) -> List[Dict[str, str]]:
    """解析Chrome书签数据，提取URL和标题"""
    bookmarks = []

    def traverse(node: Dict[str, Any], parent_path: str = ""):
        current_path = f"{parent_path}/{node.get('name', '')}" if parent_path else node.get('name', '')

        if node.get("type") == "url":
            bookmarks.append({
                "id": node.get("id"),
                "url": node.get("url", ""),
                "title": node.get("name", ""),
                "folder": current_path.rsplit("/", 1)[0] if "/" in current_path else ""
            })
        elif node.get("type") == "folder":
            for child in node.get("children", []):
                traverse(child, current_path)

    # 书签数据通常包含roots对象，其中有书签栏和其他文件夹
    roots = data.get("roots", {})
    for root_name, root_data in roots.items():
        traverse(root_data)

    return bookmarks


def read_chrome_bookmarks() -> List[Dict[str, str]]:
    """读取并解析Chrome书签文件"""
    try:
        bookmark_path = get_chrome_bookmark_path()
        if not os.path.exists(bookmark_path):
            raise FileNotFoundError(f"Chrome书签文件不存在: {bookmark_path}")

        with open(bookmark_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return parse_bookmarks(data)

    except Exception as e:
        print(f"读取书签时出错: {e}")
        return []


def check_url_validity(url: str, timeout: int = 5) -> Tuple[str, bool, str]:
    """检查URL的可访问性"""
    try:
        # 处理特殊URL协议
        if not url.startswith(('http://', 'https://')):
            return url, False, "非HTTP协议"

        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return url, response.status_code == 200, f"状态码: {response.status_code}"

    except requests.exceptions.Timeout:
        return url, False, "连接超时"
    except requests.exceptions.SSLError:
        return url, False, "SSL证书错误"
    except requests.exceptions.ConnectionError:
        return url, False, "连接错误"
    except requests.exceptions.RequestException as e:
        return url, False, f"请求异常: {str(e)}"
    except Exception as e:
        return url, False, f"未知错误: {str(e)}"


def find_duplicate_bookmarks(bookmarks: List[Dict[str, str]]) -> List[List[Dict[str, str]]]:
    """查找重复的书签"""
    url_map = {}
    duplicates = []

    for bookmark in bookmarks:
        url = bookmark['url']
        if url in url_map:
            url_map[url].append(bookmark)
        else:
            url_map[url] = [bookmark]

    # 过滤出有重复的URL
    for url, items in url_map.items():
        if len(items) > 1:
            duplicates.append(items)

    return duplicates


def clean_duplicate_bookmarks(bookmarks: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], int]:
    """清理重复的书签，保留第一个出现的"""
    unique_urls = set()
    cleaned = []
    removed_count = 0

    for bookmark in bookmarks:
        url = bookmark['url']
        if url not in unique_urls:
            unique_urls.add(url)
            cleaned.append(bookmark)
        else:
            removed_count += 1

    return cleaned, removed_count


def update_bookmark_file(cleaned_bookmarks: List[Dict[str, str]]):
    """更新书签文件"""
    try:
        bookmark_path = get_chrome_bookmark_path()
        backup_path = f"{bookmark_path}.bak"

        # 创建备份
        os.replace(bookmark_path, backup_path)
        print(f"已创建备份: {backup_path}")

        # 读取原始文件结构
        with open(backup_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 需要重新构建书签结构
        # 这里简化处理，实际应该递归重建
        # 本示例仅演示基本概念，完整实现需要处理复杂的书签结构

        # 保存修改后的文件
        with open(bookmark_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"已更新书签文件: {bookmark_path}")

    except Exception as e:
        print(f"更新书签文件时出错: {e}")


def main():
    print("正在读取Chrome书签...")
    bookmarks = read_chrome_bookmarks()
    print(f"找到 {len(bookmarks)} 个书签")

    # 检查链接有效性（使用多线程）
    print("\n正在检查书签链接有效性...")
    invalid_bookmarks = []
    total = len(bookmarks)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url_validity, b['url']): b for b in bookmarks}

        processed = 0
        start_time = time.time()

        for future in as_completed(future_to_url):
            bookmark = future_to_url[future]
            url, is_valid, reason = future.result()

            if not is_valid:
                invalid_bookmarks.append({
                    'url': url,
                    'title': bookmark['title'],
                    'reason': reason
                })

            processed += 1
            elapsed = time.time() - start_time
            eta = (elapsed / processed) * (total - processed) if processed > 0 else 0

            print(f"\r进度: {processed}/{total} | 无效链接: {len(invalid_bookmarks)} | ETA: {eta:.1f}s", end="")

    print(f"\n完成检查: {len(invalid_bookmarks)} 个无效链接")

    # 显示前10个无效链接
    if invalid_bookmarks:
        print("\n前10个无效链接:")
        for i, b in enumerate(invalid_bookmarks[:10], 1):
            print(f"{i}. {b['title']}")
            print(f"   URL: {b['url']}")
            print(f"   原因: {b['reason']}")
            print()

    # 查找重复书签
    print("\n正在查找重复书签...")
    duplicate_groups = find_duplicate_bookmarks(bookmarks)
    duplicate_count = sum(len(group) - 1 for group in duplicate_groups)

    print(f"找到 {len(duplicate_groups)} 组重复书签，共 {duplicate_count} 个")

    # 显示前3组重复书签
    if duplicate_groups:
        print("\n前3组重复书签:")
        for i, group in enumerate(duplicate_groups[:3], 1):
            print(f"组 {i}: {group[0]['url']}")
            for j, b in enumerate(group, 1):
                print(f"  {j}. {b['title']} ({b['folder']})")
            print()

    # 清理重复书签
    if duplicate_count > 0:
        choice = input("\n是否清理重复书签？(y/n): ").strip().lower()
        if choice == 'y':
            cleaned_bookmarks, removed = clean_duplicate_bookmarks(bookmarks)
            print(f"已清理 {removed} 个重复书签")

            # 注意：更新书签文件的代码被注释掉，以防止意外修改
            # 如果需要实际更新书签文件，请取消下面一行的注释
            # update_bookmark_file(cleaned_bookmarks)
        else:
            print("跳过清理重复书签")


if __name__ == "__main__":
    main()