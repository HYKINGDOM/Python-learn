import pandas as pd


def generate_sql_from_excel(file_path):
    try:
        # 尝试读取 Excel 文件
        df = pd.read_excel(file_path)  # 显式指定引擎
        print(f"读取的 DataFrame:\n{df.head()}")  # 打印前几行数据以检查读取情况

        sql_statements = {}

        # 检查是否有缺失值
        if df.isnull().values.any():
            print("数据中存在缺失值:")
            print(df[df.isnull().any(axis=1)])

        # 获取每个分配员对应的客户名称列表
        for index, row in df.iterrows():
            username = row['分配员']
            ad_id = row['客户名称']

            if pd.isna(username) or pd.isna(ad_id):
                continue

            if username not in sql_statements:
                sql_statements[username] = []

            sql_statements[username].append(ad_id)

        # 打印每个分配员的数据条数和具体的ID列表
        for username, ad_ids in sql_statements.items():
            print(f"分配员: {username}")
            print(f"客户名称数量: {len(ad_ids)}")
            print(f"客户名称列表: {', '.join(map(str, ad_ids))}")
            print()

        return sql_statements
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except ImportError:
        print("缺少依赖模块，请安装 openpyxl: pip install openpyxl")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    # 请替换为你的 Excel 文件路径
    file_path = 'D:\\download\\2025-04-10_143258.xlsx'
    sqls = generate_sql_from_excel(file_path)
    if sqls:
        for username, ad_ids in sqls.items():
            print(f"分配员: {username}")
            print(f"客户名称数量: {len(ad_ids)}")
            print(f"客户名称列表: {', '.join(map(str, ad_ids))}")
            print()
