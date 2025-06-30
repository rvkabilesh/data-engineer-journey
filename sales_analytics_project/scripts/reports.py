import pandas as pd
import sqlite3

def connect_db(filepath = 'sales_analytics_project/db/sales.db' ):
    return sqlite3.connect(filepath)

def report_by_product(conn):
    df = pd.read_sql_query('select product, sum(revenue) as total_revenue from sales group by product order by total_revenue desc',conn)
    df.to_csv('sales_analytics_project/reports/product_summary.csv', index=False)
    return df

def report_by_city(conn):
    df = pd.read_sql_query('select city, sum(quantity), sum(revenue) as total_revenue from sales group by city order by total_revenue desc', conn)
    df.to_csv('sales_analytics_project/reports/city_summary.csv',index=False)
    return df

def report_by_date(conn):
    df = pd.read_sql_query('select date, sum(revenue) from sales group by date order by date', conn)
    df.to_csv('sales_analytics_project/reports/daily_summary.csv', index=False)
    return df

if __name__ == '__main__':
    conn = connect_db()

    print("\n Report: Revenue by Product")
    print(report_by_product(conn))

    print("\n Report: Revenue by City")
    print(report_by_city(conn))

    print("\n Report: Revenue by Date")
    print(report_by_date(conn))

    conn.close()