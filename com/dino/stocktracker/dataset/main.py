import pathlib

import pandas as pd
import yfinance as yf

ticker_strings = []


# To add new Stocks to Ticker
def fetch_tickers():
    user_input: str = input("Enter Stock name to load into data frame:")
    new_stocks_list = user_input.split()

    if ticker_strings == "":
        ticker_strings.append(new_stocks_list)
    else:
        ticker_strings.extend(new_stocks_list)

    print(f'Fetching the stock data using yfinance library for: ', ticker_strings)

    df_list = list()
    for ticker in ticker_strings:
        data = yf.download(ticker, group_by="Ticker", start="2022-01-01")
        data['Ticker'] = ticker  # added this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    print(f'Stock Data extraction is completed...')

    # Prepare data frame by passing the list using pandas
    df = pd.concat(df_list)
    print(f'Preparing the dataframe...')
    # save to csv
    df.to_csv('stock_data.csv')


def check_initial_dataset():
    file = pathlib.Path("stock_data.csv")

    if file.exists():
        print(f"Dataset exists already! \n Reading from file 'stock_data.csv'...")
    else:
        fetch_tickers()
        print(f"Stock Data is downloaded to file 'stock_data.csv'...!")


def check_pivot_dataset():
    from com.dino.stocktracker.indicators.cpr_pivot_math import calculate_pivots

    file1 = pathlib.Path('stock_pivot_data.csv')

    if file1.exists():
        print(f"Pivot Dataset exists already! \n Reading from file 'stock_pivot_data.csv'...")
    else:
        user_input1 = input(f'Do you want to calculate pivots for stock data? \n Yes  or No \n')
        print(user_input1)

        if user_input1 == 'Yes':
            calculate_pivots()
        else:
            print(f'You chose not to calculate pivots')


check_initial_dataset()

check_pivot_dataset()
