from pg8000 import Connection
import pandas as pd
import getpass

def get_conn():
    return Connection(
        database='postgres',
        user=getpass.getuser())

def create_table(conn, table_name, dtypes):
    try:
        sql_cols = [f'{col_name} {dtype}' for col_name, dtype in dtypes.items()]
        sql_cols_str = ', '.join(sql_cols)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({sql_cols_str});'

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data(conn, table_name, df):
    try:
        cursor = conn.cursor()

        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        # # Insert each row from the DataFrame
        for row in df.itertuples(index=False, name=None):
            cursor.execute(query, row)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data into table: {e}")

def close_connection(conn):
    conn.close()
