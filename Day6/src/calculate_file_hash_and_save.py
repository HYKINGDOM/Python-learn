import os
import hashlib
from collections import defaultdict
from multiprocessing import Pool, cpu_count
import psycopg2

# 数据库连接配置
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'user_7YNTcH',
    'password': 'password_x6B4tc',
    'host': '192.168.5.4',
    'port': 5432
}

def calculate_file_hash(file_path, hash_algorithm='md5', chunk_size=8192, sample_size=1024 * 1024):
    """计算文件的哈希值"""
    hash_func = hashlib.new(hash_algorithm)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        hash_func.update(f.read(min(sample_size, file_size)))
        if file_size > sample_size * 3:
            f.seek(file_size // 2)
            hash_func.update(f.read(sample_size))
            f.seek(-sample_size, os.SEEK_END)
            hash_func.update(f.read(sample_size))
    return hash_func.hexdigest()

def find_all_files(root_dir):
    """递归查找所有文件"""
    all_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            all_files.append(file_path)
    return all_files

def get_file_metadata(file_path):
    """获取文件的元数据"""
    try:
        file_size = os.path.getsize(file_path) // 1024  # 文件大小（KB）
        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_name)[1].lower()
        hash_value = calculate_file_hash(file_path)
        return {
            'file_name': file_name,
            'file_type': file_type,
            'hash_value': hash_value,
            'file_size': file_size,
            'file_path': file_path,
            'encoding_type': None  # 假设编码方式未知
        }
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def check_existing_hashes(hashes):
    """检查数据库中是否已存在相同的哈希值"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    placeholders = ','.join(['%s'] * len(hashes))
    query = f"SELECT hash_value FROM file_metadata WHERE hash_value IN ({placeholders})"
    cursor.execute(query, hashes)
    existing_hashes = {row[0] for row in cursor.fetchall()}
    cursor.close()
    conn.close()
    return existing_hashes

def insert_files_to_db(files):
    """批量插入文件到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO file_metadata (file_name, file_type, hash_value, file_size, file_path, encoding_type)
    VALUES (%(file_name)s, %(file_type)s, %(hash_value)s, %(file_size)s, %(file_path)s, %(encoding_type)s)
    ON CONFLICT (hash_value) DO NOTHING;
    """
    cursor.executemany(insert_query, files)
    conn.commit()
    cursor.close()
    conn.close()

def main(root_dirs):
    all_files = []
    for root_dir in root_dirs:
        print(f"Scanning directory: {root_dir}")
        all_files.extend(find_all_files(root_dir))

    # 仅处理前100个文件
    all_files = all_files[:100]

    print(f"Found {len(all_files)} files across all directories.")

    # 使用多进程计算文件元数据
    with Pool(cpu_count()) as pool:
        file_metadata_list = pool.map(get_file_metadata, all_files)

    # 过滤掉处理失败的文件
    file_metadata_list = [meta for meta in file_metadata_list if meta is not None]

    # 提取所有哈希值
    hashes = [meta['hash_value'] for meta in file_metadata_list]

    # 检查数据库中已存在的哈希值
    existing_hashes = check_existing_hashes(hashes)

    # 过滤出需要插入的新文件
    new_files = [meta for meta in file_metadata_list if meta['hash_value'] not in existing_hashes]

    print(f"Found {len(new_files)} new files to insert into the database.")

    # 批量插入新文件
    if new_files:
        insert_files_to_db(new_files)
        print(f"Inserted {len(new_files)} new files into the database.")
    else:
        print("No new files to insert.")

if __name__ == "__main__":
    # root_directories = [
    #     "X:\\WeGame", "Y:\\video", "Z:\\downloads", "Z:\\videos",
    #     "F:\\迅雷下载", "F:\\win", "G:\\新建文件夹", "L:\\图书", "M:\\学习文档"
    # ]

    root_directories = ["J:\\新建文件夹"
    ]
    main(root_directories)
