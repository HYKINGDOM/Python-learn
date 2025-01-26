import re

import pandas as pd
import pymysql
from sqlalchemy import create_engine


class DatabaseManager:
    def __init__(self, host='localhost', user='root', password='your_password', database='your_database'):
        self.connection_params = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'charset': 'utf8mb4'
        }
        self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4")

    def clean_identifier(self, identifier):
        """清理标识符（表名、列名等）"""
        if identifier:
            # 移除特殊字符，保留字母、数字和下划线
            cleaned = re.sub(r'[^\w]', '_', str(identifier))
            # 确保不以数字开头
            if cleaned[0].isdigit():
                cleaned = 'f_' + cleaned
            return cleaned
        return 'unnamed'

    def determine_sql_type(self, column_name):
        """根据列名确定SQL数据类型"""
        column_name = column_name.lower()

        if 'id' in column_name and ('jsid' in column_name or column_name == 'id'):
            return 'BIGINT'
        elif any(word in column_name for word in ['date', 'time', '日期', '时间']):
            return 'DATETIME'
        elif any(word in column_name for word in ['price', 'amount', 'ratio', 'rate', '价格', '金额', '比率']):
            return 'DECIMAL(20,4)'
        elif any(word in column_name for word in ['code', '代码']):
            return 'VARCHAR(50)'
        elif any(word in column_name for word in ['name', 'desc', '名称', '描述']):
            return 'VARCHAR(255)'
        else:
            return 'VARCHAR(100)'

    def generate_create_tables(self, table_relations_file, data_dict_file):
        """生成建表DDL语句"""
        # 读取CSV文件
        tables_df = pd.read_csv(table_relations_file)
        columns_df = pd.read_csv(data_dict_file)

        ddl_statements = []

        # 遍历每个表
        for _, table_row in tables_df.iterrows():
            table_name = self.clean_identifier(table_row['表英文'])
            table_comment = table_row['表描述'].replace("'", "''") if pd.notna(table_row['表描述']) else ''

            # 获取该表的所有列
            table_columns = columns_df[columns_df.iloc[:, 0] == table_name]

            if table_columns.empty:
                continue

            columns_ddl = []
            for _, column in table_columns.iterrows():
                col_name = self.clean_identifier(column.iloc[1])  # 第二列是字段名
                col_type = self.determine_sql_type(col_name)
                col_comment = column.iloc[2].replace("'", "''") if pd.notna(column.iloc[2]) else ''  # 第三列是字段描述

                column_def = f"{col_name} {col_type}"
                if col_name.lower() == 'id':
                    column_def += " PRIMARY KEY AUTO_INCREMENT"

                column_def += f" COMMENT '{col_comment}'"
                columns_ddl.append(column_def)

            create_table_sql = f"""
DROP TABLE IF EXISTS {table_name};
CREATE TABLE {table_name} (
    {',\n    '.join(columns_ddl)}
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='{table_comment}';
"""
            ddl_statements.append(create_table_sql)

        return ddl_statements

    def generate_insert_statements(self, data_dict_file):
        """生成INSERT语句"""
        columns_df = pd.read_csv(data_dict_file)
        insert_statements = []

        # 按表分组处理
        for table_name, group in columns_df.groupby(columns_df.columns[0]):
            clean_table_name = self.clean_identifier(table_name)
            columns = [self.clean_identifier(col) for col in group.iloc[:, 1]]  # 第二列是字段名

            # 生成INSERT语句模板
            insert_sql = f"""
INSERT INTO {clean_table_name} 
({', '.join(columns)}) 
VALUES 
({', '.join(['%s'] * len(columns))});
"""
            insert_statements.append(insert_sql)

        return insert_statements

    def execute_sql_files(self, ddl_statements, insert_statements):
        """执行SQL语句"""
        try:
            # 使用pymysql执行DDL语句
            conn = pymysql.connect(**self.connection_params)
            with conn.cursor() as cursor:
                # 执行建表语句
                for ddl in ddl_statements:
                    cursor.execute(ddl)

                # 执行INSERT语句
                for insert in insert_statements:
                    cursor.execute(insert)

                conn.commit()
            print("SQL语句执行成功！")

        except Exception as e:
            print(f"执行SQL时发生错误: {str(e)}")
            conn.rollback()
        finally:
            conn.close()


def main():
    # 配置数据库连接参数
    db_manager = DatabaseManager(
        host='10.0.201.34',
        user='root',
        password='mysql_F44EQG',
        database='data_database'
    )

    # 生成SQL语句
    ddl_statements = db_manager.generate_create_tables(
        'D:\project\github\Python-learn\Day27\src\data\数据字典-库表关系 .csv',
        'D:\project\github\Python-learn\Day27\src\data\数据字典  - 副本.csv'
    )
    insert_statements = db_manager.generate_insert_statements('D:\project\github\Python-learn\Day27\src\data\数据字典  - 副本.csv')

    # 将SQL语句写入文件（用于审查）
    with open('output/create_tables.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(ddl_statements))

    with open('output/insert_data.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(insert_statements))

    # 执行SQL语句
    db_manager.execute_sql_files(ddl_statements, insert_statements)


if __name__ == "__main__":
    main()
