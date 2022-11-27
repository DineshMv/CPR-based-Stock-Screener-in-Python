import time
class myStockScreener:
    def __init__(self, from_date, to_date, timer):
        self.timer = timer
        self.from_date = from_date
        self.to_date = to_date

    def start_app(self):
        from com.dino.stocktracker.Dataset.get_dataset import check_initial_dataset, check_pivot_dataset

        check_initial_dataset(self.from_date, self.to_date)
        check_pivot_dataset(self.from_date, self.to_date)

        from com.dino.stocktracker.Find_pivots.filter_narrow_range import find_narrow_cpr
        find_narrow_cpr()

        from com.dino.stocktracker.Mail_alerts.stock_alerts import send_alerts
        send_alerts()

    def run(self):
        print(f"Hi, I am Shelbot\U0001F60E!\nWelcome to my Project - 'CPR based Stock Screener in Python'")
        time.sleep(self.timer)
        print()
        user_name = str(input('What is your name?\n'))
        print()
        print(f'Shelbot\U0001F60E: Hello, {user_name} \U0001F60D')
        time.sleep(self.timer)
        print()
        print(f"Shelbot\U0001F60E: {user_name}, I'll help you with the application!")
        time.sleep(self.timer)
        print(f'________________________________________________________________________________')
        # from run import start_app, initialise_app
        self.start_app()
        time.sleep(self.timer)
        print()
        print(f"Shelbot\U0001F60E: That's all with the application for now, {user_name}")
        time.sleep(self.timer)
        print(
            f'Shelbot\U0001F60E: Have a good day!\nShelbot\U0001F60E: Bye, {user_name} \U0001F60D\U0001F60D\U0001F60D')


app = myStockScreener("2022-11-22", "2022-11-24", 1.5)

app.run()


# Backtesting function:
def perform_backtesting(from_date, to_date):
    from com.dino.stocktracker.Indicator_backtests.backtest import start_backtesting
    user_inp1 = int(input(
        f"Shelbot\U0001F60E: Do you want to perform backtesting to find Narrow CPR accuracy with Weekly Stock data? "
        f"\n 1. 'Yes'  or 2. 'No' \n"))

    if user_inp1 == 1:
        start_backtesting(from_date, to_date)
    elif user_inp1 == 2:
        print(f'Shelbot\U0001F60E: You chose not to perform backtesting')
    else:
        print(f"Shelbot\U0001F60E: Your input is wrong, Please check again")

# perform_backtesting('2019-12-30', '2022-10-30')
