import pathlib

import pandas as pd

from config import dataset_path


def find_narrow_cpr():
    df = pd.read_csv(dataset_path + 'stock_data.csv', index_col=0, parse_dates=True)
    df1 = pd.DataFrame()
    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        user_inp1 = int(
            input(f"Shelbot\U0001F60E: Do you want to filter Narrow range stocks from the entire dataset? \n 1. 'Yes' "
                  f" or 2. 'No' \n"))

        if user_inp1 == 1:
            print(f"Shelbot\U0001F60E: Reading from file 'stock_data.csv'...")
            # Filter for only days with Narrow Range CPR
            df1 = df[df['NR-CPR'].str.contains('Yes')]
            df1.to_csv(dataset_path + 'Narrow_CPR.csv')
            print(f"Shelbot\U0001F60E: Stock Tracker has been downloaded to 'Narrow_CPR.csv'")
        else:
            print(f'Shelbot\U0001F60E: You chose not to filter the stocks')
    else:
        print(f'Shelbot\U0001F60E: Pivots are not generated yet!')
    print(f'________________________________________________________________________________')
# find_narrow_cpr()
