from utils import fetch_exchange_data,transform_rates
from db import init_db, insert_data

raw_data = fetch_exchange_data('EUR')
df = transform_rates(raw_data)
#print(df)

import sqlite3
import pandas as pd

con = sqlite3.connect('Day 16.5 query_latest\currency.db')
init_db('Day 16.5 query_latest\currency.db')
insert_data(df,con)

latest = pd.read_sql_query("""
SELECT * FROM exchange_rates


""", con)

print(" Most Recent Records:\n", latest)