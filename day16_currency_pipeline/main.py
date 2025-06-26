from utils import fetch_exchange_data, transform_rates
from db import init_db, insert_data
import pandas as pd

def main():
    raw_data = fetch_exchange_data()
    df = transform_rates(raw_data)

    print(df.head())

    conn = init_db()
    insert_data(df,conn)

    df1 = pd.read_sql_query('select * from exchange_rates where rate < 1',conn)
    print(df1)

    conn.close()

if __name__ == '__main__':
    main()


