import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.0f}'.format)  # 禁用科学计数法


def print_excel_data(sales):
    # 获取数据框的行数和列数
    # 获取前五行数据
    subset = sales.head(5)

    # 每行打印五列数据
    for i in range(0, 5):
        start_idx = i * 5  # 每行起始的索引
        end_idx = (i + 1) * 5  # 每行结束的索引
        print(subset.iloc[:, start_idx:end_idx])  # 打印当前行的数据
        print()  # 换行


# 定义一个函数，用于将纵坐标的值除以1000，并添加 'k' 作为单位
# 定义一个自定义的格式化函数，将纵坐标的值除以1000，并显示为整数
def format_cost(value, _):
    return f'{int(value / 1000):,}'


if __name__ == '__main__':
    # 指定header=None，并使用names参数定义列名
    column_names = ['id', 'agent_id', 'agent_name', 'advertiser_id', 'advertiser_name', 'first_industry', 'second_industry', 'account_source', 'company_name', 'audit_pass_time', 'account_status', 'register_time', 'cost', 'cash_cost', 'bid_cost', 'brand_cost', 'grants_cost', 'cpc_cost', 'cpm_cost', 'ocpc_cost', 'cpa_cost', 'ocpm_cost', 'cpv_cost', 'cpt_cost', 'gd_cost', 'show', 'cpm', 'click', 'ctr', 'cpc', 'transfer_count', 'today_cost', 'transfer_amount', 'history_cost', 'register_days', 'first_cost_time', 'cash_balance', 'rant_balance', 'year', 'month', 'day', 'date', 'is_sync', 'native_province_cost', 'out_province_cost', 'out_province_ids', 'is_sync_native', 'first_recharge_amount', 'first_recharge_time', 'last_renew_time', 'total_renew_number', 'total_balance', 'valid_balance', 'is_sycn_actual', 'saler_user_id', 'saler_user_name', 'saler_dept_id', 'saler_dept_name', 'oper_user_id', 'oper_user_name', 'oper_dept_id', 'oper_dept_name', 'create_time', 'create_user', 'update_time', 'update_user', 'remark', 'del_flag']
    sales = pd.read_csv('D:\\datasets\\dspAdvertiserCost_202406.csv', dtype='object', header=None, names=column_names)

    print(sales.info())  # 查看数据概览
    print(sales.shape)  # 文件有多少行,多少列
    print(sales.head())  # 查看文件的部分数据，用head函数显示头部数据，默认5行

    # 将 'cost' 列的数据转换为数值类型，如果无法转换，则设置为 NaN 值。errors='coerce' 参数用于将无法转换的值设置为 NaN。
    sales['cost'] = pd.to_numeric(sales['cost'], errors='coerce')
    sales['cash_cost'] = pd.to_numeric(sales['cash_cost'], errors='coerce')
    sales['bid_cost'] = pd.to_numeric(sales['bid_cost'], errors='coerce')
    sales['brand_cost'] = pd.to_numeric(sales['brand_cost'], errors='coerce')
    sales['grants_cost'] = pd.to_numeric(sales['grants_cost'], errors='coerce')
    sales['advertiser_id'] = pd.to_numeric(sales['advertiser_id'], errors='coerce')
    sales['date'] = pd.to_datetime(sales['date'], format='%Y-%m-%d', errors='coerce')

    sales = sales[(sales['cost'] != 0.00) & (sales['cost'] != 0)]

    print(sales.describe())

    # 按日期（'date'）字段进行分组，并计算每天的 'cost' 总和
    daily_sales = sales.groupby('date')['cost'].sum()

    print(daily_sales)
    # 创建一个日期格式化器，用于调整横坐标显示的日期格式
    date_format = mdates.DateFormatter('%Y-%m-%d')

    # 绘制趋势图
    fig, ax = plt.subplots()
    ax.plot(daily_sales.index, daily_sales.values)
    ax.xaxis.set_major_formatter(date_format)  # 设置横坐标的日期格式
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10, integer=True, min_n_ticks=5))  # 设置纵坐标刻度范围和间隔
    plt.xlabel('Date')
    plt.ylabel('Total Cost')
    plt.title('Daily Cost Trend')
    plt.xticks(rotation=45)  # 旋转横坐标刻度标签，以免重叠
    plt.tight_layout()  # 调整图像布局，以免标签被裁剪
    plt.show()
