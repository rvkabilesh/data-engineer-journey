from utils import fetch_exchange_data,transform_rates
from db import init_db

raw_data = fetch_exchange_data('EUR')
json_data = transform_rates(raw_data)
print(json_data)

import sqlite3
import pandas as pd

con = sqlite3.connect('Day 16.5 query_latest\currency.db')
init_db(con)

latest = pd.read_sql_query("""
SELECT * FROM exchange_rates
ORDER BY Timestamp DESC
""", con).head()

print(" Most Recent Records:\n", latest)