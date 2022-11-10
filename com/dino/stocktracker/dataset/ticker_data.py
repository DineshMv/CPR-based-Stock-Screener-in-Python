import yfinance as yf
import pandas as pd
import pathlib

ticker_strings = []

# To add new Stocks to Ticker
def fetch_tickers():
    user_input = input("Enter Stock name to load into data frame:")
    new_stocks_list = user_input.split()
    if ticker_strings == "":
        new_ticker_strings = ticker_strings.append(new_stocks_list)
    else:
        new_ticker_strings = ticker_strings.extend(new_stocks_list)

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
    df.to_csv('ticker_data.csv')


file = pathlib.Path("ticker_data.csv")

if file.exists():
    print(f"Dataset exists already! \n Reading from data file 'ticker_data.csv'...")
else:
    fetch_tickers()
    print(f"Stock Data is downloaded to file 'ticker_data.csv'...!")
