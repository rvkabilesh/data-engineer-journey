import pandas as pd
import requests

def fetch_exchange_data(base = 'USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base}'
    res = requests.get(url)

    fake_response = res.json()
    #fake_response.pop('rates')  # removeed the key on purpose

    return fake_response

import datetime

def transform_rates(json_data):
    if 'rates' not in json_data:
        print("Error: 'rates' key missing in response.")
        return pd.DataFrame()

    df = pd.DataFrame(json_data['rates'].items(), columns=['Currency', 'Rate'])
    df['Base'] = json_data['base']
    df['Date'] = json_data['date']
    df['Timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    return df






