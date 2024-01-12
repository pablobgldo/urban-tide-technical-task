from pg8000 import Connection
import getpass


# Connects to default Postgres database 'postgres' using login name of user.
# Uses default values for password, host and port number.
def get_conn():
    return Connection(
        database='postgres',
        user=getpass.getuser())


# Creates table if it does not exist with column names and types.
# Needs connection, table name and dictionary generated by 'infer_data_types'.
def create_table(conn, table_name, dtypes):
    try:
        # Creates list of 'column name' with 'data type' items.
        sql_cols = [f'{col} {dtype}' for col, dtype in dtypes.items()]
        # Creates part of the string needed for SQL query.
        sql_cols_str = ', '.join(sql_cols)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({sql_cols_str});'

        cursor = conn.cursor()
        # Runs SQL query to create table with desired query.
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error creating table {table_name}: {e}")


# Inserts data into table specified.
def insert_data(conn, table_name, df):
    try:
        cursor = conn.cursor()
        # Creates a string with column names separated by comma.
        columns = ', '.join(df.columns)
        # Creates a string with value placeholders separated by comma.
        placeholders = ', '.join(['%s'] * len(df.columns))
        # Creates generic SQL insertion query.
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        # Inserts each row of values from the DataFrame into table specified.
        for row in df.itertuples(index=False, name=None):
            cursor.execute(query, row)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data into table {table_name}: {e}")


# Closes connection to database.
def close_conn(conn):
    conn.close()
