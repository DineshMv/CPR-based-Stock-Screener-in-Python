from com.dino.stocktracker.config import *

# mylist = ['AAPL', 'AMZN', 'GOOG', 'TSLA']
mylist = wkly_stock_list


def start_backtesting(mylist):
    from com.dino.stocktracker.backtesting.cpr_backtest import get_wkly_data
    get_wkly_data(mylist)

    from com.dino.stocktracker.backtesting.cpr_backtest import calculate_pivots
    calculate_pivots(mylist)

    from com.dino.stocktracker.backtesting.cpr_backtest import get_stats
    get_stats(mylist)


for ticker in mylist:
    start_backtesting([ticker])
