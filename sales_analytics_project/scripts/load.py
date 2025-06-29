import pandas as pd 
import sqlite3
from ingest import load_sales_csv
from transform import clean_sales_data

def init_db(db_path = 'db/sales.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
create table if not exists sales(
                   Date text,
                   Product text,
                   Quantity integer,
                   Price real,
                   City text,
                   Customer text,
                   Revenue real
)''')

    conn.commit()
    return conn

def insert_data(df,conn):
    df.to_sql('sales', conn, if_exists = 'append', index = False)
    print("✅ Data inserted into database")

if __name__ == '__main__':
    df_raw = load_sales_csv('./sales_analytics_project/data/raw_sales.csv')
    df_clean = clean_sales_data(df_raw)

    conn = init_db('./sales_analytics_project/db/sales.db')
    insert_data(df_clean, conn)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    print(df)
    conn.close()
    