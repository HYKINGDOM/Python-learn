import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import yfinance as yf
from psycopg2 import sql

# 该方法使用时需要开启VPN
if __name__ == '__main__':
    tickerName = 'GBTC'

    # 获取GBTC股票的历史数据
    data = yf.download(tickerName, start='2020-01-01', end='2024-12-25', ignore_tz=True)

    # 绘制GBTC收盘价的时间序列图
    data['Close'].plot(title=tickerName + ' Stock Closing Price', figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

    # 连接到PostgreSQL数据库
    conn = psycopg2.connect(
        host='10.0.201.34',
        port='5432',
        dbname='user_tZGjBb',
        user='user_tZGjBb',
        password='password_fajJed'
    )
    cur = conn.cursor()

    insert_query = sql.SQL("""
        INSERT INTO stock_data (date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s);
        """)

    # 将数据插入到表中
    for index, row in data.iterrows():
        # 确保 index 是 pandas.Timestamp 类型
        if isinstance(index, pd.Timestamp):
            date = index.to_pydatetime().date()
        else:
            # 如果 index 不是 pandas.Timestamp 类型，尝试将其转换为 datetime 对象
            date = pd.to_datetime(index).date()

        print(row.iloc[0])  # Open
        print(row.iloc[1])  # High
        print(row.iloc[2])  # Low
        print(row.iloc[3])  # Close

        cur.execute(insert_query, (
            date,
            row.iloc[0],
            row.iloc[1],
            row.iloc[2],
            row.iloc[3],
            row.iloc[4]
        ))

    conn.commit()
    cur.close()
    conn.close()
