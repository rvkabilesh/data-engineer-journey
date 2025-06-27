import pandas as pd

def load_sales_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        print('✅ file ingested!!!')
        return df

    except Exception as e:
        print('Cannot ingest!!')
        return None
    
if __name__ == '__main__':
    df = load_sales_csv('./sales_analytics_project/data/raw_sales.csv')
    print(df.head())
