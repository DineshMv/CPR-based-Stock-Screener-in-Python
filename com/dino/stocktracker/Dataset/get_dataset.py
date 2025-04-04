import pathlib

import pandas as pd
import yfinance as yf

from config import dataset_path, all_mcap_stocks

# List of Medium to Mega Market Capital stock in NASDAQ, NYSE:
ticker_strings = []
mega_tickers = all_mcap_stocks


# stock_tracker_ticker = ['AAPL', 'AMZN', 'GOOG', 'TSLA', 'MSFT', 'XOM', 'JNJ']

def fetch_from_yfinance(stock_list, time_period):
    df_list = list()
    # Fetch and clean data
    for stock in stock_list:
        stock_selected = yf.Ticker(stock)
        print(f'Shelbot\U0001F60E: Scrapping historical data for:', stock)
        data = (
            stock_selected.history(period=time_period)
            .drop(columns=['Dividends', 'Stock Splits'])
            .round(2)
            .assign(Volume=lambda x: x['Volume'].astype(int))
            .reset_index()
        )

        # Add Ticker Name in column-1
        data['Ticker'] = stock

        # Convert Date format to MM/DD/YYYY
        data['Date'] = data['Date'].dt.strftime('%m/%d/%Y')

        # Reorder columns
        data = data[['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        df_list.append(data)

        # Reset index
        df = pd.concat(df_list, ignore_index=False)
        df = df.set_index(['Ticker', 'Date'])

    # save to csv
    df.to_csv(dataset_path + 'stock_data.csv')
    print(f"Shelbot\U0001F60E: Dataset 'stock_data.csv' is generated!")


def fetch_tickers(time_period):
    user_input = int(input("Shelbot\U0001F60E: Do you want to create stock tracker with list of USA Medium - Mega "
                           "MCAP stocks: \n 1. 'Yes' or 2. 'No' \n"))

    if user_input == 1:
        print(f'Shelbot\U0001F60E: Fetching the stock data using yfinance library for:\n ', mega_tickers)
        fetch_from_yfinance(mega_tickers, time_period)
        print(f"Shelbot\U0001F60E: Stock Data is downloaded to file 'stock_data.csv'...!")

    elif user_input == 2:
        user_inp2 = input("Shelbot\U0001F60E: Provide the list of stocks you want to create a tracker: \n")
        new_stocks_list = user_inp2.split()
        ticker_strings.extend(new_stocks_list)
        print(f'Shelbot\U0001F60E: List of stocks selected:', ticker_strings)
        fetch_from_yfinance(ticker_strings, time_period)
        # print(f"Shelbot\U0001F60E: Stock Data is downloaded to file 'stock_data.csv'...!")

    else:
        if not 1 or 2:
            raise Exception(" Shelbot\U0001F60E: Please choose to enter either 1 or 2 options")
    print(f'________________________________________________________________________________')


def check_initial_dataset(time_period):
    file = pathlib.Path(dataset_path + "stock_data.csv")
    if file.exists():
        user_in = int(input(f"Shelbot\U0001F60E: Do you want to use existing dataset? \n 1. 'Yes' or 2. 'No'\n"))
        if user_in == 1:
            print(f"Shelbot\U0001F60E: Existing Dataset - 'stock_data.csv' is selected")
        elif user_in == 2:
            fetch_tickers(time_period)
    else:
        fetch_tickers(time_period)
    print(f'________________________________________________________________________________')


def check_pivot_dataset(time_period):
    from com.dino.stocktracker.Find_pivots.calculate_pivots import calculate_pivots

    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        user_inp1 = int(
            input(f"Shelbot\U0001F60E: Do you want to calculate pivots for stock data? \n 1. 'Yes'  or 2. 'No' \n"))

        if user_inp1 == 1:
            calculate_pivots(time_period)
        elif user_inp1 == 2:
            print(f'Shelbot\U0001F60E: You chose not to calculate pivots')
    else:
        print(f"Shelbot\U0001F60E: Please generate OHLC data with your preferred list of stocks!")
    print(f'________________________________________________________________________________')


check_initial_dataset("1mo")
# check_pivot_dataset('1mo')
