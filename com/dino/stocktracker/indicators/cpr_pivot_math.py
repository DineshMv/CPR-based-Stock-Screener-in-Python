import pandas as pd

path = 'D:/Stock_Indicator/com/dino/stocktracker/dataset/'

df1 = pd.read_csv('../dataset/ticker_data.csv', index_col=0, parse_dates=True)
dt_range = pd.date_range(start="2022-01-01", end="  2022-10-31")
df1 = df1[df1.index.isin(dt_range)]
print(f'Reading from initial data source... ')

df2 = pd.DataFrame()

# ******************Formulae**************************
# central pivot range
# pivot = (high + low + close) /3
# BC = (high + low) / 2
# TC = (pivot - BC) + pivot

# 3  Support levels
# S1 = (pivot * 2) - high
# S2 = pivot - (high - low)
# S3 = low - 2 * (high - pivot)
#
#
# 3 Resistance levels
# R1 = (pivot * 2) - low
# R2 = pivot + (high - low)
# R3 = high + 2 * (pivot-low)


# Derive a new column from existing column

# Pivot Levels

df2['Pivot'] = (df1['High'] + df1['Low'] + df1['Close']) / 3
df2['BC'] = (df1['High'] + df1['Low']) / 2
df2['TC'] = (df2['Pivot'] - df2['BC']) + df2['Pivot']
print(f'Calculating Pivot Values...')

# 3  Support Levels

df2['S1'] = (df2['Pivot'] * 2) - df1['High']
df2['S2'] = df2['Pivot'] - (df1['High'] - df1['Low'])
df2['S3'] = df1['Low'] - 2 * (df1['High'] - df2['Pivot'])
print(f'Calculating Support Values...')

# 3 Resistance Levels

df2['R1'] = (df2['Pivot'] * 2) - df1['Low']
df2['R2'] = df2['Pivot'] + (df1['High'] - df1['Low'])
df2['R3'] = df1['High'] + 2 * (df2['Pivot'] - df1['Low'])
print(f'Calculating Resistance Values...')

# print(df2.head(5))

result = pd.concat([df1, df2], axis=1, join='inner')
# print(result)

# Export Pivot Data to a new Data Set
result.to_csv(path + 'stock_data.csv')
print(f'Pivot data is appended to initial dataset')
