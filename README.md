# Automated Stock Tracker with SMTP Alerts:

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://raw.githubusercontent.com/DineshMv/CPR-based-Stock-Screener-in-Python/master/LICENSE)

I created Stock Tracker app based on leading indicator - Central Pivot Range(CPR)

## Table of Contents

+ [About](#About)
+ [Central Pivot Range - Overview](#CPR_Overview)
	+ [Strategies with CPR](#Strategies_with_CPR)
		+ [Width of CPR](#Width_CPR)
		+ [Virgin CPR](#Virgin_CPR)
+ [Pivots Math Formula](#Pivots_Formula)
+ [Project Structure](#Project_Structure)
+ [Libraries used](#Libraries)
+ [Back Testing Results](#BackTesting_Results)
+ [License](#License)

## About: <a name = "About"></a>

- This application uses a leading technical indicator - **Central Pivot Range** which uses previous OHLC data and
  predict the next day/week/month pivots.
- Using this indicator principles such as **Narrow Range CPR**, we are identifying the list of stocks which can have a
  huge momentum for next day/week/month.
- Email alerts will be sent with this filtered list of stocks
- We also identified the accuracy of this indicator by comparing the previous momentum on normal days with momentum on
  Narrow Range CPR days.

## Central Pivot Range - Overview: <a name = "CPR_Overview"></a>

Central Pivot Range Indicator is a powerful price action leading indicator. The range acts as major support or
resistance for every stock. Anyone can forecast the trend of any stock, whether it will be bullish, bearish or sideways,
by looking at the width of the CPR.

### Strategies with CPR: <a name = "Strategies_with_CPR"></a>

Major Strategies that are in practise with CPR are:

- ### Width of CPR: <a name = "Width_CPR"></a>
  Width of CPR can be categorized into 3 parts:
  1. Narrow Range CPR - NRCPR
  2. Medium Range CPR - MRCPR
  3. Wide Range CPR - WRCPR

	1. **NRCPR** says that - whenever a stock trades within a small range in the previous day, week or month, depending
	   on the CPR you are using, then there is a good possibility of a trending day.

	2. **MRCPR** says that - When the range of CPR is neither too narrow nor too wide,then it indicates that the stock
	   will not be as trending as much as a narrow range.

	3. **WRCPR** says that: When the range of the CPR is very wide, then the stock was trending in the previous sessions
	   which indicates a high possibility of a sideways day.

- ### Virgin CPR: <a name = "Virgin CPR"></a>
  A virgin CPR occurs when all the candles on a trading session have closed either upside or downside of the CPR, and
  none of the candles closed at the CPR. A Virgin CPR acts as very strong support and resistance for next few subsequent
  trading sessions.

## Pivots Math Formula: <a name = "Pivots_Formula"></a>

```
	Central Pivots:
	  - pivot = (high + low + close) /3
	  - BC = (high + low) / 2
	  - TC = (pivot - BC) + pivot
	
	Support levels:
	  - S1 = (pivot * 2) - high
	  - S2 = pivot - (high - low)
	  - S3 = low - 2 * (high - pivot)
	
	Resistance levels:
	  - R1 = (pivot * 2) - low
	  - R2 = pivot + (high - low)
	  - R3 = high + 2 * (pivot-low)
	
	Formula for Narrow Range = 2*(Pivot - BC)<0.0015*close
```

## Project Structure:<a name = "Project_Structure"></a>

```
	.
	└── Stock Screener/
		├── com/
		│   └── dino/
		│       └── stocktracker/
		│           ├── Dataset/
		│           │   └── get_dataset.py/
		│           │       ├── stock_data.csv
		│           │       ├── Narrow_CPR.csv
		│           │       └── wkly_dataset.csv
		│           ├── Find Pivots/
		│           │   ├── find_pivots.py
		│           │   └── filter_narrow_range.py
		│           ├── Indicator Backtests/
		│           │   ├── backtest.py
		│           │   └── cpr_backtest.py
		│           └── Mail Alerts/
		│               └── stock_alerts.py
		├── run.py
		├── config.py
		├── README.md
		├── .gitignore
		├── CODE_OF_CONDUCT.md
		└── LICENSE
```

- Note: config.py is restricted to local as it contains secret credentials

## Libraries used:<a name = "Libraries"></a>

- pathlib
- pandas
- yfinance
- mplfinance
- smtplib
- email.mime

## Back Testing Results:<a name = "BackTesting_Results"></a>

- We performed back testing with a list of Top 100 US stocks(as of 11/25/2022) and calculated the accuracy of Narrow CPR
  indicator based on momentum

| Time Period |   From   |     To     | Success Ratio | Fail Ratio |
|:-----------:|:--------:|:----------:|:-------------:|:----------:|
|   2 Years   | 2020/1/1 | 10/30/2022 |     58.59     |   41.41    |
|   5 Years   | 2017/1/1 | 10/30/2022 |     59.18     |   40.82    |
|  10 Years   | 2012/1/1 | 10/30/2022 |     59.73     |   40.27    |
|  20 Years   | 2022/1/1 | 10/30/2022 |     59.61     |   40.39    |

## License:<a name = "License"></a>

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://raw.githubusercontent.com/DineshMv/CPR-based-Stock-Screener-in-Python/master/LICENSE)
