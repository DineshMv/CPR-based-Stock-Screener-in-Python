import pandas as pd

path = 'D:/Stock_Indicator/com/dino/stocktracker/dataset/'

df = pd.read_csv('../dataset/stock_pivot_data.csv', index_col=0, parse_dates=True)
dt_range = pd.date_range(start="2022-01-01", end="  2022-10-31")
df = df[df.index.isin(dt_range)]


def find_narrow_cpr():
    # Filter for only days with Narrow CPR
    print(df[df['NR-CPR'].str.contains("Yes", na=False)])


find_narrow_cpr()
