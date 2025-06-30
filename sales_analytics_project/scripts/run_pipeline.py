from ingest import load_sales_csv
from transform import clean_sales_data
from load import init_db, insert_data
from reports import report_by_product, report_by_city, report_by_date
import pandas as pd

def run():
    print("🚀 Running Full Sales Pipeline...")

    # Ingest
    df_raw = load_sales_csv('sales_analytics_project/data/raw_sales.csv')

    # Transform
    df_clean = clean_sales_data(df_raw)

    # Load
    conn = init_db('sales_analytics_project/db/sales.db')
    insert_data(df_clean, conn)

    # Report
    report_by_product(conn)
    report_by_city(conn)
    report_by_date(conn)

    conn.close()
    print("✅ Pipeline run completed successfully.")

if __name__ == '__main__':
    run()
