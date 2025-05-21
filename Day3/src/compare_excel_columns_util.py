import pandas as pd


def compare_excel_sheets(file_path):
    try:
        # 读取 Excel 文件
        excel_file = pd.ExcelFile(file_path)

        # 获取 sheet1 和 sheet2 的 A 列数据并转换为列表
        sheet1_col_a = excel_file.parse('Sheet1')['客户ID'].tolist()
        sheet2_col_a = excel_file.parse('Sheet2')['customer_id'].tolist()

        # 将两个列表排序以实现数据对齐比较
        sheet1_sorted = sorted(sheet1_col_a)
        sheet2_sorted = sorted(sheet2_col_a)

        # 找出不同的元素及其原始索引
        different_items = []

        # 使用集合快速查找差异元素
        set_sheet1 = set(sheet1_sorted)
        set_sheet2 = set(sheet2_sorted)

        # 找出在 sheet1 中但不在 sheet2 中的元素
        diff_sheet1 = list(set_sheet1 - set_sheet2)
        # 找出在 sheet2 中但不在 sheet1 中的元素
        diff_sheet2 = list(set_sheet2 - set_sheet1)

        for item in diff_sheet1:
            different_items.append(('Sheet1', item))
        for item in diff_sheet2:
            different_items.append(('Sheet2', item))

        return different_items

    except FileNotFoundError:
        print("错误：未找到指定的 Excel 文件。")
    except KeyError:
        print("错误：Excel 文件中不存在指定的工作表或列。")
    except Exception as e:
        print(f"发生未知错误：{e}")

    return []


if __name__ == "__main__":
    file_path = 'D:\\document\\adv.xlsx'
    result = compare_excel_sheets(file_path)
    if result is not None:
        print("数据不同的行索引为：", result)
