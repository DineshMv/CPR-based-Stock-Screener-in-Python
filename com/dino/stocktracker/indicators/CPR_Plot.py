import mplfinance as mpf
import pandas as pd

idf = pd.read_csv('../dataset/stock_data.csv', index_col=0, parse_dates=True)
df = idf.loc['2022-7-01':'2022-10-31', :]

apd = mpf.make_addplot(df, color='Black', width=0.5, ylim=(10, 80), secondary_y=True)

mpf.plot(df, ylabel_lower='RSI', type='candle',
         style='yahoo', volume=True, mav=(3, 7),
         figscale=1.5, addplot=apd, panel_ratios=(2, 0.5))
