import pandas as pd
import requests

def fetch_data_rates(base='USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base}'
    response = requests.get(url)
    return response.json()

def process_rates(data):
    rates = data['rates']
    df_rates = pd.DataFrame(rates.items(), columns = ['currency', 'rates'])
    return df_rates.sort_values('rates')

def save_data(df,filename):
    df.to_csv(f'exchange rates/{filename}',index=False)

