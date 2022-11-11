import pathlib

import pandas as pd

from com.dino.stocktracker.config import dataset_path

df = pd.read_csv(dataset_path + 'stock_data.csv', index_col=0, parse_dates=True)

df2 = pd.DataFrame()


def find_narrow_cpr():
    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        print(f"Reading from file 'stock_data.csv'...")
        # Filter for only days with Narrow Range CPR
        df2 = df[df['NR-CPR'].str.contains('Yes')]
        df2.to_csv(dataset_path + 'Narrow_CPR.csv')
        print(f"Stock Tracker has been downloaded to 'Narrow_CPR.csv'")
    else:
        print(f'Pivots are not generated yet!')


find_narrow_cpr()
