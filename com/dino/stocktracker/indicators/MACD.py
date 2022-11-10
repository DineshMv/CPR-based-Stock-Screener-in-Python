import pandas as pd
import mplfinance as mpf

import matplotlib.dates as mdates

idf = pd.read_csv('../dataset/ticker_data.csv', index_col=0, parse_dates=True)
df = idf.loc['2022-08-01':'2022-10-31', :]

# =======
#  MACD:

exp12 = df['Close'].ewm(span=12, adjust=False).mean()
exp26 = df['Close'].ewm(span=26, adjust=False).mean()
macd = exp12 - exp26
signal = macd.ewm(span=9, adjust=False).mean()
histogram = macd - signal

fb_green = dict(y1=macd.values, y2=signal.values, where=signal < macd, color="#93c47d", alpha=0.5, interpolate=True)
fb_red = dict(y1=macd.values, y2=signal.values, where=signal > macd, color="#e06666", alpha=0.5, interpolate=True)
fb_green['panel'] = 1
fb_red['panel'] = 1
fb = [fb_green, fb_red]

apds = [mpf.make_addplot(exp12, color='red', width=0.5),
        mpf.make_addplot(exp26, color='c', width=0.5),
        mpf.make_addplot(histogram, type='bar', width=0.5, panel=1, color='dimgray', alpha=1, secondary_y=True),
        mpf.make_addplot(macd, panel=1, width=0.5, color='fuchsia', secondary_y=False),
        mpf.make_addplot(signal, panel=1, width=0.5, color='b', secondary_y=False)
        ]

s = mpf.make_mpf_style(base_mpf_style='yahoo', rc={'figure.facecolor': 'lightgray'})

mpf.plot(df, type='candle', addplot=apds, figscale=2, figratio=(6, 5), title='\n\nMACD',
         style=s, volume=True, volume_panel=2, panel_ratios=(5, 2, 1), fill_between=fb) #, show_nontrading=True)
