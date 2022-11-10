import pandas as pd

from com.dino.stocktracker.config import dataset_path

df = pd.read_csv('../dataset/stock_pivot_data.csv', index_col=0, parse_dates=True)
dt_range = pd.date_range(start="2022-01-01", end="  2022-10-31")
df = df[df.index.isin(dt_range)]

df2 = pd.DataFrame()


def find_narrow_cpr():
    # Filter for only days with Narrow CPR
    # print(df[df['NR-CPR'].str.contains("Yes", na=False)])
    df2 = df[df['NR-CPR'].str.contains("Yes", na=False)]
    df2.to_csv(dataset_path + 'nrcpr.csv')


find_narrow_cpr()
print(f"Stock Tracker has been downloaded to 'nrcpr.csv'")
