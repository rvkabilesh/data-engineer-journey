import pandas as pd

def clean_sales_data(df):
    #column 
    df.columns = df.columns.str.strip().str.title()
    #data 
    df['Date'] = pd.to_datetime(df['Date'],errors = 'coerce')
    #product
    df['Product'] = df['Product'].astype(str).str.strip().str.capitalize()
    df = df[df['Product'].str.len() > 0] #remove empty (product)
    #quantity
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype(int)
    #price
    df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace('₹','',regex = False).replace('',0),errors='coerce').astype(float)
    #city
    df['City'] = df['City'].astype(str).str.strip().str.title()
    #customer
    df['Customer'] = df['Customer'].astype(str).str.strip().str.title()
    #remove duplicates
    df = df.drop_duplicates()
    #new col -- revenue
    df['Revenue'] = df['Quantity'] * df['Price']
    print('✅ cleaned data....')

    return df

if __name__ == '__main__':
    from ingest import load_sales_csv
    df_raw = load_sales_csv('./sales_analytics_project/data/raw_sales.csv')
    df_clean = clean_sales_data(df_raw)
    print("✅ Cleaned Data:\n", df_clean)
    

