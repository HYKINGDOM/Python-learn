import pandas as pd
import pyarrow as pyarrow

if __name__ == '__main__':
    # Parquet文件路径
    parquet_file = 'G:\\迅雷下载\\Compressed\\archive\\test.parquet'
    # 读取Parquet文件为DataFrame
    df = pd.read_parquet(parquet_file, engine='pyarrow')

    # 将DataFrame保存为JSON文件
    df.to_json('G:\\迅雷下载\\Compressed\\archive\\test.csv', orient='records')

    print('Parquet文件导入MySQL完成！')