import pandas as pd


def compare_excel_columns(file_path):
    try:
        # 读取 Excel 文件
        excel_file = pd.ExcelFile(file_path)

        # 获取 sheet1 和 sheet2 的 A 列数据
        df1 = excel_file.parse('sheet1')
        df2 = excel_file.parse('sheet2')
        column1 = df1['customer_id']
        column2 = df2['customer_id']

        # 找出数据不同的行索引
        aligned_col1, aligned_col2 = pd.align(column1, column2, fill_value=None)
        diff_rows = aligned_col1 != aligned_col2
        different_indexes = diff_rows[diff_rows].index.tolist()
        return different_indexes

    except FileNotFoundError:
        print("错误：未找到指定的 Excel 文件，请检查文件路径是否正确。")
    except KeyError:
        print("错误：Excel 文件中未找到 'A' 列，请检查工作表结构。")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    file_path = 'D:\\document\\adv.xlsx'
    result = compare_excel_columns(file_path)
    if result is not None:
        print("数据不同的行索引为：", result)
