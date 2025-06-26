import os
from utils import fetch_data_rates, process_rates, save_data

def main():
        os.makedirs('day15_currency_pipeline/exchange rates', exist_ok=True)

        data = fetch_data_rates()
        df_rates = process_rates(data)
        save_data(df_rates,'exchange_rates.csv')

        strong = df_rates[df_rates['rates'] < 1]
        save_data(strong,'strong_currencies.csv')

        print('Weakest currencies:')
        print(df_rates.tail(5))

if __name__ == '__main__':
        main()