import pandas as pd

idf = pd.read_csv('../dataset/stock_data.csv', index_col=0, parse_dates=True)
df = idf.loc['2022-08-01':'2022-10-31', :]

# =======
#  MACD:

exp12 = df['Close'].ewm(span=12, adjust=False).mean()
exp26 = df['Close'].ewm(span=26, adjust=False).mean()
macd = exp12 - exp26
signal = macd.ewm(span=9, adjust=False).mean()
histogram = macd - signal

