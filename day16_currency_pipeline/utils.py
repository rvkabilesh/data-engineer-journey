import pandas as pd
import requests

def fetch_exchange_data(base = 'USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base}'
    req = requests.get(url)
    return req.json()

def transform_rates(json_data):
    rates = json_data['rates']
    date = json_data['date']
    df = pd.DataFrame(rates.items(),columns=['currency','rate'])
    df['base'] = json_data['base']
    df['date'] = date
    return df
