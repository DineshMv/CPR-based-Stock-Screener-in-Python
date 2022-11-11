# Automated Stock Tracker with SMTP Alerts: 

In this repo, I created Stock Tracker app based on indicator - Central Pivot Range(CPR)

**Technical Indicator - over view:**

	Central Pivot Range Indicator is a powerful price action leading indicator. The range acts as major support or resistance for every stock. Anyone can forecast the trend of any stock, whether it will be bullish, bearish or sideways, by looking at the width of the CPR.

Major Strategies that are best in practise are: 

1. **Width of CPR:**
		Width of CPR can be categorized into 3 parts:
		**1. Narrow Range CPR - NRCPR
		  2. Medium Range CPR - MRCPR
		  3. Wide Range CPR - WRCPR**
		
	1. **NRCPR** says that - whenever a stock trades within a small range in the previous day, week or month, depending on the CPR you are using, then there is a good possibility of a trending day.
	
	2. **MRCPR** says that - When the range of CPR is neither too narrow nor too wide,then it indicates that the stock will not be as trending as much as a narrow range.

	3. **WRCPR** says that: When the range of the CPR is very wide, then the stock was trending in the previous sessions which indicates a high possibility of a sideways day.

2. **Virgin CPR**:
	A virgin CPR occurs when all the candles on a trading session have closed either upside or downside of the CPR, and none of the candles closed at the CPR. A Virgin CPR acts as very strong support and resistance for next few subsequent trading sessions.
	
# Formulae:

# Central Pivots:
- pivot = (high + low + close) /3
- BC = (high + low) / 2
- TC = (pivot - BC) + pivot

# 3  Support levels
- S1 = (pivot * 2) - high
- S2 = pivot - (high - low)
- S3 = low - 2 * (high - pivot)

# 3 Resistance levels
- R1 = (pivot * 2) - low
- R2 = pivot + (high - low)
- R3 = high + 2 * (pivot-low)

**Formula for NRCPR = 2*(Pivot - BC)<0.0015*close**

Libraries used:
- pathlib
- pandas
- yfinance
- smtplib
- email.mime
