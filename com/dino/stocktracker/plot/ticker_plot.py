import mplfinance as mpf
import pandas as pd

# import ticker_data

df = pd.read_csv('stock_data.csv', index_col=0, parse_dates=True)
# df = pd.read_csv('CPR_Pivot_Data.csv', index_col=0, parse_dates=True)
dt_range = pd.date_range(start="2022-08-01", end="2022-10-31")
df = df[df.index.isin(dt_range)]
print(df.head())

d1 = df.index[0]
d2 = df.index[-1]

tdates = [(d1, d2)]
print(tdates)
pivots = [n for n in df.columns if n not in not_pivots]

#apd =
mpf.plot(df,
         # tlines=
         # daily,
         hlines=dict(hlines=[80, 121], colors=['g', 'r'], linestyle='-.'),
         figscale=1.33,
         type='candle',
         title='Apple, March - 2022',
         style='yahoo',
         ylabel='Price ($)',
         figratio=(12, 8),
         volume=True,
         ylabel_lower='Volume',
         show_nontrading=True,
         # savefig='ticket_info'
         )
