import pandas as pd
import mplfinance as mpf

price_chart_df = pd.read_csv('../dataset/ticker_data.csv', index_col=0, parse_dates=True)


def add_EMA(price, day):
    return price.ewm(span=day).mean()


def add_STOCH(close, low, high, period, k, d=0):
    STOCH_K = ((close - low.rolling(window=period).min()) / (
                high.rolling(window=period).max() - low.rolling(window=period).min())) * 100
    STOCH_K = STOCH_K.rolling(window=k).mean()
    if d == 0:
        return STOCH_K
    else:
        STOCH_D = STOCH_K.rolling(window=d).mean()
        return STOCH_D


def check_bounce_EMA(df):
    candle1 = df.iloc[-1]
    candle2 = df.iloc[-2]
    cond1 = candle1['EMA18'] > candle1['EMA50'] > candle1['EMA100']
    cond2 = candle1['STOCH_%K(5,3,3)'] <= 30 or candle1['STOCH_%D(5,3,3)'] <= 30
    cond3 = candle2['Low'] < candle2['EMA50'] < candle2['Close'] and \
            candle1['Low'] > candle1['EMA50']
    return cond1 and cond2 and cond3


# a list to store the screened results
screened_list = []
# get the full stock list
# price_chart_df = pd.read_csv(ticker_data.csv)
# Step 2: add technical indicators (in this case EMA)
close = price_chart_df['Close']
low = price_chart_df['Low']
open = price_chart_df['Open']
high = price_chart_df['High']
price_chart_df['EMA18'] = add_EMA(close, 18)
price_chart_df['EMA50'] = add_EMA(close, 50)
price_chart_df['EMA100'] = add_EMA(close, 100)
price_chart_df['STOCH_%K(5,3,3)'] = add_STOCH(close, low, high, 5, 3)
price_chart_df = add_STOCH(close, low, high, 5, 3, 3)


apdict = mpf.make_addplot(price_chart_df['LowerB'])
mpf.plot(price_chart_df,addplot=apdict)

mpf.plot(price_chart_df,
         type='candle',
         title='Apple, March - 2022',
         style='charles',
         ylabel='Price ($)',
         figratio=(12, 8),
         volume=True,
         ylabel_lower='Volume',
         show_nontrading=True,
         # savefig='ticket_info'
         )
