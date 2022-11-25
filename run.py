import time

from com.dino.stocktracker.backtesting.run_backtests import mylist, start_backtesting

print(f"Hi, I am Shelbot\U0001F607!")
time.sleep(1)
print(f'Let me guide you help you with the application!')
print(f'________________________________________________________________________________')


def start_app():
    from com.dino.stocktracker.dataset.get_dataset import check_initial_dataset, check_pivot_dataset

    check_initial_dataset()
    check_pivot_dataset()

    from com.dino.stocktracker.indicators.filter_narrow_cpr import find_narrow_cpr
    find_narrow_cpr()

    from com.dino.stocktracker.stock_tracker_alerts.stock_alerts import send_alerts
    send_alerts()


# start_app()


def perform_backtesting():
    user_inp1 = int(input(
        f"Shelbot\U0001F607: Do you want to perform backtesting to find Narrow CPR accuracy with Weekly Stock data? \n 1. 'Yes'  or 2. 'No' \n"))

    if user_inp1 == 1:
        start_backtesting(mylist)
    elif user_inp1 == 2:
        print(f'Shelbot\U0001F607: You chose not to perform backtesting')
    else:
        print(f"Shelbot\U0001F607: Your input is wrong, Please check again")


start_app()

perform_backtesting()
