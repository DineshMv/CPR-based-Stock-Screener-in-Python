import pathlib

import pandas as pd
import yfinance as yf

from com.dino.stocktracker.config import *

ticker_strings = []

# List of Medium to Mega Market Capital stock in NASDAQ, NYSE:
# stock_tracker_ticker = TOP_MCAP_Stocks


# To add new Stocks to Ticker
stock_tracker_ticker = ['AAPL', 'AMZN', 'GOOG', 'TSLA', 'MSFT']


def fetch_from_yfinance(user_choice):
    df_list = list()
    for ticker in user_choice:
        data = yf.download(ticker, group_by="Ticker", start=start_date, end=end_date)
        data['Ticker'] = ticker  # added this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    print(f'Shelbot\U0001F607: Stock Data extraction from YFinance is completed...')

    # Prepare data frame by passing the list using pandas
    df = pd.concat(df_list)
    print(f'Shelbot\U0001F607: Preparing the dataframe...')
    # save to csv
    df.to_csv(dataset_path + 'stock_data.csv')


def fetch_tickers():
    user_input = int(input(
        "Shelbot\U0001F607: Do you want to create stock tracker with list of USA Medium - Mega MCAP stocks: \n 1. 'Yes' "
        "or 2. 'No' \n"))

    if user_input == 1:
        print(f'Shelbot\U0001F607: Fetching the stock data using yfinance library for: ', stock_tracker_ticker)
        fetch_from_yfinance(stock_tracker_ticker)
        print(f"Shelbot\U0001F607: Stock Data is downloaded to file 'stock_data.csv'...!")

    elif user_input == 2:
        user_inp2 = input("Shelbot\U0001F607: Provide the list of stocks you want to create a tracker: \n")
        new_stocks_list = user_inp2.split()
        ticker_strings.extend(new_stocks_list)
        print(f'Shelbot\U0001F607: Fetching the stock data using yfinance library for: ', ticker_strings)
        fetch_from_yfinance(ticker_strings)
        print(f"Shelbot\U0001F607: Stock Data is downloaded to file 'stock_data.csv'...!")

    else:
        if not 1 or 2:
            raise Exception(" Shelbot\U0001F607: Please choose to enter either 1 or 2 options")
    print(f'________________________________________________________________________________')


def check_initial_dataset():
    file = pathlib.Path(dataset_path + "stock_data.csv")

    if file.exists():
        user_in = int(input(f"Shelbot\U0001F607: Do you want to use existing dataset? \n 1. 'Yes' or 2. 'No'\n"))
        if user_in == 1:
            print(f"Shelbot\U0001F607: Existing Dataset - 'stock_data.csv' is selected")
        elif user_in == 2:
            fetch_tickers()
    else:
        fetch_tickers()
    print(f'________________________________________________________________________________')


def check_pivot_dataset():
    from com.dino.stocktracker.indicators.find_pivots import calculate_pivots

    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        user_inp1 = int(
            input(f"Shelbot\U0001F607: Do you want to calculate pivots for stock data? \n 1. 'Yes'  or 2. 'No' \n"))

        if user_inp1 == 1:
            calculate_pivots()
        elif user_inp1 == 2:
            print(f'Shelbot\U0001F607: You chose not to calculate pivots')
    else:
        print(f"Shelbot\U0001F607: Please generate OHLC data with your preferred list of stocks!")
    print(f'________________________________________________________________________________')

# check_initial_dataset()
#
# check_pivot_dataset()
