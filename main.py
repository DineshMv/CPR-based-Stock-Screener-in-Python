import pathlib

import pandas as pd
import yfinance as yf

from com.dino.stocktracker.config import *

ticker_strings = []

# List of Medium to Mega Market Capital stock in NASDAQ, NYSE:
stock_tracker_ticker = ['AAPL', 'ABCB', 'ABMD', 'ACAD',
                        'ACHC', 'ACIW', 'ACLS', 'ACT', 'ADBE', 'ADI', 'ADSK', 'AFRM', 'AGNC', 'AHCO', 'ALGM', 'ALGN',
                        'ALHC', 'ALNY',
                        'ALRM', 'ALTR', 'AMAT', 'AMBA', 'AMD', 'AMED', 'AMGN', 'AMKR', 'AMLX', 'ANSS', 'APLS', 'APP',
                        'APPF', 'APPN',
                        'ARCC', 'ARRY', 'ARVN', 'ARWR', 'AUB', 'AVGO', 'AVT', 'AXNX', 'AXSM', 'AZPN', 'AZTA', 'BANF',
                        'BANR', 'BCRX',
                        'BEAM', 'BHF', 'BIIB', 'BL', 'BLKB', 'BMBL', 'BMRN', 'BOKF', 'BPMC', 'BPOP', 'BRZE', 'BSY',
                        'CACC', 'CATY', 'CBSH',
                        'CDNS', 'CERE', 'CERT', 'CFLT', 'CG', 'CINF', 'CLBK', 'CME', 'CNXC', 'COIN', 'COLB', 'COOP',
                        'CORT', 'COUP',
                        'CRUS', 'CRVL', 'CRWD', 'CSGP', 'CSQ', 'CTSH', 'CVBF', 'CVLT', 'CVT', 'CYTK', 'DBX', 'DDOG',
                        'DIOD', 'DNLI',
                        'DOCU', 'DUOL', 'DXCM', 'EBC', 'EEFT', 'ENPH', 'ENSG', 'ENTG', 'EQIX', 'EQRX', 'ERIE', 'EWBC',
                        'EXAS', 'EXEL',
                        'EXLS', 'EYE', 'FCNCA', 'FFBC', 'FFIN', 'FFIV', 'FHB', 'FIBK', 'FITB', 'FIVN', 'FLYW', 'FOCS',
                        'FOLD', 'FRME',
                        'FROG', 'FRSH', 'FSLR', 'FTNT', 'FULT', 'GBDC', 'GEN', 'GFS', 'GH', 'GILD', 'GLPI', 'GOOG',
                        'GOOGL', 'GTLB',
                        'HALO', 'HBAN', 'HCP', 'HLNE', 'HOLX', 'HOOD', 'HQY', 'HRMY', 'HSIC', 'HST', 'HTLF', 'HWC',
                        'IART', 'IBKR', 'IBOC',
                        'IBTX', 'ICUI', 'IDXX', 'ILMN', 'INCY', 'INDB', 'INSM', 'INTC', 'INTU', 'IONS', 'IPGP', 'IRTC',
                        'ISEE', 'ISRG',
                        'ITCI', 'JAMF', 'JKHY', 'KLAC', 'KNBE', 'KRTX', 'LAMR', 'LEGN', 'LFUS', 'LHCG', 'LITE', 'LKFN',
                        'LNTH', 'LOGI',
                        'LPLA', 'LRCX', 'LSCC', 'LYFT', 'MANH', 'MASI', 'MCHP', 'MDB', 'MEDP', 'META', 'MKTX', 'MMSI',
                        'MORN', 'MPWR',
                        'MQ', 'MRNA', 'MRTX', 'MSFT', 'MTCH', 'MTSI', 'MU', 'MXL', 'NARI', 'NATI', 'NAVI', 'NBIX',
                        'NBTB', 'NCNO', 'NDAQ',
                        'NEOG', 'NSIT', 'NTAP', 'NTCT', 'NTLA', 'NTNX', 'NTRA', 'NTRS', 'NVDA', 'OKTA', 'OLED', 'OMCL',
                        'ON', 'ONB',
                        'ONEM', 'OPCH', 'OZK', 'PACW', 'PANW', 'PAYO', 'PCH', 'PCRX', 'PCTY', 'PCVX', 'PDCO', 'PECO',
                        'PEGA', 'PFG',
                        'PGNY', 'PINC', 'PLXS', 'PNFP', 'PODD', 'POWI', 'PPBI', 'PRFT', 'PRGS', 'PROK', 'PRTA', 'PRVA',
                        'PSEC', 'PTC',
                        'PTCT', 'PYCR', 'QCOM', 'QDEL', 'QLYS', 'RARE', 'REG', 'REGN', 'RGEN', 'RLAY', 'RMBS', 'RNST',
                        'RPRX', 'RUM',
                        'RXDX', 'SANM', 'SBAC', 'SBNY', 'SBRA', 'SEIC', 'SFNC', 'SGEN', 'SGRY', 'SHLS', 'SIGI', 'SIVB',
                        'SLAB', 'SLM',
                        'SMCI', 'SNPS', 'SOFI', 'SPLK', 'SPSC', 'SPT', 'SPWR', 'SRPT', 'SSB', 'SSNC', 'STAA', 'SWAV',
                        'SWKS', 'SYBT',
                        'SYNA', 'SYNH', 'TCBI', 'TECH', 'TENB', 'TFSL', 'TNDM', 'TOWN', 'TPG', 'TRMK', 'TROW', 'TTD',
                        'TTWO', 'TW', 'TWKS',
                        'TXG', 'TXN', 'UBSI', 'UCBI', 'UMBF', 'UMPQ', 'UTHR', 'VERX', 'VIAV', 'VICR', 'VIR', 'VIRT',
                        'VLY', 'VRNT', 'VRSN',
                        'VRTX', 'VSAT', 'VTRS', 'WAFD', 'WDAY', 'WDC', 'WSBC', 'WSFS', 'WTFC', 'XM', 'XMTR', 'XRAY',
                        'XRX', 'ZBRA', 'ZI',
                        'ZION', 'ZM', 'ZS']


# To add new Stocks to Ticker
# stock_tracker_ticker = ['AAPL', 'AMZN', 'GOOG', 'TSLA', 'MSFT']


def fetch_from_yfinance(user_choice):
    df_list = list()
    for ticker in user_choice:
        data = yf.download(ticker, group_by="Ticker", start=start_date, end=end_date)
        data['Ticker'] = ticker  # added this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    print(f'Stock Data extraction from YFinance is completed...')

    # Prepare data frame by passing the list using pandas
    df = pd.concat(df_list)
    print(f'Preparing the dataframe...')
    # save to csv
    df.to_csv(dataset_path + 'stock_data.csv')


def fetch_tickers():
    user_input = int(input(
        "Do you want to create stock tracker with list of USA Medium - Mega MCAP stocks: \n 1. 'Yes' "
        "or 2. 'No' \n"))

    if user_input == 1:
        print(f'Fetching the stock data using yfinance library for: ', stock_tracker_ticker)
        fetch_from_yfinance(stock_tracker_ticker)
        print(f"Stock Data is downloaded to file 'stock_data.csv'...!")

    elif user_input == 2:
        user_inp2 = input("Provide the list of stocks you want to create a tracker: \n")
        new_stocks_list = user_inp2.split()
        ticker_strings.extend(new_stocks_list)
        print(f'Fetching the stock data using yfinance library for: ', ticker_strings)
        fetch_from_yfinance(ticker_strings)
        print(f"Stock Data is downloaded to file 'stock_data.csv'...!")

    else:
        if not 1 or 2:
            raise Exception(" Please choose to enter either 1 or 2 options")


def check_initial_dataset():
    file = pathlib.Path(dataset_path + "stock_data.csv")

    if file.exists():
        user_in = int(input(f"Do you want to use existing dataset? \n 1. 'Yes' or 2. 'No'\n"))
        if user_in == 1:
            print(f"Reading from existing Dataset 'stock_data.csv'...")
        elif user_in == 2:
            fetch_tickers()
    else:
        fetch_tickers()


def check_pivot_dataset():
    from com.dino.stocktracker.indicators.find_pivots import calculate_pivots

    file = pathlib.Path(dataset_path + 'stock_data.csv')

    if file.exists():
        user_inp1 = int(input(f"Do you want to calculate pivots for stock data? \n 1. 'Yes'  or 2. 'No' \n"))

        if user_inp1 == 1:
            calculate_pivots()
        elif user_inp1 == 2:
            print(f'You chose not to calculate pivots')
    else:
        print(f"Please generate OHLC data with your preferred list of stocks!")


check_initial_dataset()

check_pivot_dataset()
