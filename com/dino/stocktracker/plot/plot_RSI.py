import mplfinance as mpf
import pandas as pd

from com.dino.stocktracker.indicators import RSI

df = pd.read_csv('../dataset/ticker_data.csv', index_col=0, parse_dates=True).iloc[0:100]

df['rsi'] = RSI.relative_strength(df['Close'], n=14)

# print(df.head())
# print(df.tail())

apd = mpf.make_addplot(df['rsi'], panel=2, color='Black', width=0.5, ylim=(10, 80), secondary_y=True)
mpf.plot(df, ylabel_lower='RSI', type='candle',
         style='yahoo', volume=True, mav=(10, 20),
         figscale=1.5, addplot=apd, panel_ratios=(2, 0.8))
