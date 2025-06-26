import sqlite3

def init_db(db_name = 'day16_currency_pipeline/currency.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
create table if not exists exchange_rates(
                   currency text,
                   rate REAL,
                   base text,
                   date text
)''')

    conn.commit()
    return conn

def insert_data(df,conn):
    df.to_sql('exchange_rates',conn,if_exists = 'append',index = False) 

