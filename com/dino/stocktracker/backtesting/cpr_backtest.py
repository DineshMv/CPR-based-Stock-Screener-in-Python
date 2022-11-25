import pandas as pd
import yfinance as yf

from com.dino.stocktracker.config import *


def get_wkly_data(mylist):
    df_list = list()
    for stocks in mylist:
        print(f'Shelbot\U0001F607: Fetching the stock data using yfinance library for: ', stocks)
        data = yf.download(stocks, interval='1wk', group_by="Ticker", start=wkly_from_date, end=wkly_to_date)
        data['Ticker'] = stocks
        # added this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)

    # Prepare data frame by passing the list using pandas
    df = pd.concat(df_list)

    # save to csv
    df.to_csv(dataset_path + 'wkly_dataset.csv')


# get_wkly_data()

def calculate_pivots(mylist):
    df = pd.read_csv(dataset_path + 'wkly_dataset.csv', index_col=0, parse_dates=True)
    dt_range = pd.date_range(start=wkly_from_date, end=wkly_to_date)
    df = df[df.index.isin(dt_range)]
    df1 = pd.DataFrame()

    # find  momentum and Momentum Ratio
    # Momentum = Close - Prev.Close &  # Momentum Ratio = (Momentum / Prev.Momentum)

    df1['prevClose'] = df['Close'].shift(1)
    df1['Momentum'] = abs(df['Close'] - df1['prevClose'])
    df1['MomentumRatio'] = abs(df1['Momentum'] / df1['Momentum'].shift(1))

    df1['MomentumType'] = df1['MomentumRatio'].values < 1.5
    df1['MomentumType'] = df1['MomentumType'].replace([True, False], ['Less Momentum', 'Strong Momentum'])

    # Calculate Pivots:
    df1['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
    df1['BC'] = (df['High'] + df['Low']) / 2
    df1['TC'] = (df1['Pivot'] - df1['BC']) + df1['Pivot']

    # Narrow Range Condition: abs(2* Pivot - 2* BC) < (close * 0.001): boolean
    df1['NR-CPR'] = (abs(2 * df1['Pivot'] - 2 * df1['BC']) < 0.0025 * df['Close'])
    df1['NR-CPR'] = df1['NR-CPR'].replace([True, False], ['Yes', 'No'])
    df1['NR-CPR'] = df1['NR-CPR'].shift(1)

    result = pd.concat([df, df1], axis=1)

    # Export Pivot Data to a new Data Set
    result.to_csv(dataset_path + 'wkly_dataset.csv')
    print(f"Shelbot\U0001F607: Weekly Stock - Pivot Data is downloaded to 'wkly_dataset.csv'")
    print(f'-------------------------------------------------------------------------------')


# calculate_pivots()

def get_stats(mylist):
    df = pd.read_csv(dataset_path + 'wkly_dataset.csv', index_col=0, parse_dates=True)
    df = df.dropna()
    df1 = df[df['NR-CPR'].str.contains('Yes')]

    for stock in mylist:
        df2 = df1[df1['Ticker'].str.contains(stock)]
        success_ratio = 100 * len(df2[df2['MomentumType'].str.contains('Strong Momentum')]) / len(df2['MomentumType'])
        success_ratio = round(success_ratio, 2)
        failed_ratio = 100 * len(df2[df2['MomentumType'].str.contains('Less Momentum')]) / len(df2['MomentumType'])
        failed_ratio = round(failed_ratio, 2)
        print(
            f"Success ratio for {stock}: {success_ratio}% & Failed ratio for {stock}: {failed_ratio}% || Total Momentum days: {len(df2['MomentumType'])}")

# get_stats()
