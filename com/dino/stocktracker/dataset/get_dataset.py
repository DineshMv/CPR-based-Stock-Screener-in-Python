import pathlib

import pandas as pd
import yfinance as yf

from com.dino.stocktracker.config import all_mcap_stocks, dataset_path

# List of Medium to Mega Market Capital stock in NASDAQ, NYSE:
ticker_strings = []
stock_tracker_ticker = all_mcap_stocks


# stock_tracker_ticker = ['AAPL', 'AMZN', 'GOOG', 'TSLA', 'MSFT']


def fetch_from_yfinance(user_choice, from_date, to_date):
    df_list = list()
    for ticker in user_choice:
        data = yf.download(ticker, group_by="Ticker", start=from_date, end=to_date)
        data['Ticker'] = ticker  # added this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    print(f'Shelbot\U0001F60E: Stock Data extraction from YFinance is completed...')

    # Prepare data frame by passing the list using pandas
    df = pd.concat(df_list)
    print(f'Shelbot\U0001F60E: Preparing the dataframe...')
    # save to csv
    df.to_csv(dataset_path + 'stock_data.csv')


def fetch_tickers(from_date, to_date):
    user_input = int(input("Shelbot\U0001F60E: Do you want to create stock tracker with list of USA Medium - Mega "
                           "MCAP stocks: \n 1. 'Yes' or 2. 'No' \n"))

    if user_input == 1:
        print(f'Shelbot\U0001F60E: Fetching the stock data using yfinance library for:\n ', stock_tracker_ticker)
        fetch_from_yfinance(stock_tracker_ticker, from_date, to_date)
        print(f"Shelbot\U0001F60E: Stock Data is downloaded to file 'stock_data.csv'...!")

    elif user_input == 2:
        user_inp2 = input("Shelbot\U0001F60E: Provide the list of stocks you want to create a tracker: \n")
        new_stocks_list = user_inp2.split()
        ticker_strings.extend(new_stocks_list)
        print(f'Shelbot\U0001F60E: Fetching the stock data using yfinance library for: ', ticker_strings)
        fetch_from_yfinance(ticker_strings, from_date, to_date)
        print(f"Shelbot\U0001F60E: Stock Data is downloaded to file 'stock_data.csv'...!")

    else:
        if not 1 or 2:
            raise Exception(" Shelbot\U0001F60E: Please choose to enter either 1 or 2 options")
    print(f'________________________________________________________________________________')


def check_initial_dataset(from_date, to_date):
    file = pathlib.Path(dataset_path + "stock_data.csv")

    if file.exists():
        user_in = int(input(f"Shelbot\U0001F60E: Do you want to use existing dataset? \n 1. 'Yes' or 2. 'No'\n"))
        if user_in == 1:
            print(f"Shelbot\U0001F60E: Existing Dataset - 'stock_data.csv' is selected")
        elif user_in == 2:
            fetch_tickers(from_date, to_date)
    else:
        fetch_tickers(from_date, to_date)
    print(f'________________________________________________________________________________')


def check_pivot_dataset(from_date, to_date):
    from com.dino.stocktracker.indicators.find_pivots import calculate_pivots

    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        user_inp1 = int(
            input(f"Shelbot\U0001F60E: Do you want to calculate pivots for stock data? \n 1. 'Yes'  or 2. 'No' \n"))

        if user_inp1 == 1:
            calculate_pivots(from_date, to_date)
        elif user_inp1 == 2:
            print(f'Shelbot\U0001F60E: You chose not to calculate pivots')
    else:
        print(f"Shelbot\U0001F60E: Please generate OHLC data with your preferred list of stocks!")
    print(f'________________________________________________________________________________')

# check_initial_dataset()
#
# check_pivot_dataset()
