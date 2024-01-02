import pandas as pd
from sqlalchemy import create_engine
import pymysql
import pyarrow as pyarrow

# MySQL数据库连接信息
mysql_host = 'localhost'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'root'
mysql_database = 'test_demo'



if __name__ == '__main__':
    # Parquet文件路径
    parquet_file = 'G:\\迅雷下载\\Compressed\\archive\\test.parquet'

    # 创建MySQL数据库连接
    engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true&rewriteBatchedStatements=true')

    # 读取Parquet文件为DataFrame
    df = pd.read_parquet(parquet_file, engine='pyarrow')

    print(df.columns)

    # 写入MySQL数据库
    df.to_sql('pubg_data', engine, if_exists='replace', index=False)

    print('Parquet文件导入MySQL完成！')