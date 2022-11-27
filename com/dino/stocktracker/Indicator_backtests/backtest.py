# mylist = wkly_stock_list

mylist = ['AAPL', 'NFLX', 'AMZN', 'GOOG', 'TSLA']


def start_backtesting(from_date, to_date):
    # for ticker in mylist:
    from com.dino.stocktracker.Indicator_backtests.cpr_backtest import get_wkly_data
    get_wkly_data(mylist, from_date, to_date)

    from com.dino.stocktracker.Indicator_backtests.cpr_backtest import calculate_pivots
    calculate_pivots(mylist, from_date, to_date)

    from com.dino.stocktracker.Indicator_backtests.cpr_backtest import get_stats
    get_stats(mylist)

# for ticker in mylist:
#     start_backtesting([ticker])

