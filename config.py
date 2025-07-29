username = "xxxxx"
my_pwd = ""
mymail = 'xxxxxx@gmail.com'
mail_list = ["xxxx@gmail.com", "Xxxx@gmail.com"]
dataset_path = 'xxxx/stocktracker/Dataset/'
# start_date = "2022-11-23"
# end_date = "2022-11-24"

all_mcap_stocks = ['AAPL', 'ABCB', 'ABMD', 'ACAD',
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

# Top 100 MCAP:
wkly_stock_list = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'BRK-B', 'TSLA', 'UNH', 'XOM', 'JNJ', 'V', 'WMT', 'NVDA', 'JPM',
                   'CVX',
                   'PG', 'LLY', 'MA', 'HD', 'BAC', 'META', 'ABBV', 'PFE', 'KO', 'MRK', 'PEP', 'COST', 'ORCL', 'AVGO',
                   'TMO',
                   'MCD', 'CSCO', 'DHR', 'TMUS', 'ABT', 'WFC', 'DIS', 'NEE', 'BMY', 'NKE', 'VZ', 'TXN', 'UPS', 'COP',
                   'ADBE',
                   'CMCSA', 'CRM', 'PM', 'MS', 'SCHW', 'AMGN', 'HON', 'RTX', 'QCOM', 'T', 'IBM', 'DE', 'CVS', 'GS',
                   'UNP',
                   'NFLX', 'LOW', 'LMT', 'CAT', 'AMD', 'INTC', 'ELV', 'SPGI', 'AXP', 'SBUX', 'INTU', 'BLK', 'ADP',
                   'GILD',
                   'PLD', 'BA', 'AMT', 'CI', 'GE', 'TJX', 'ISRG', 'C', 'AMAT', 'PYPL', 'MDLZ', 'SYK', 'ADI', 'MMC',
                   'EOG',
                   'NOW', 'VRTX', 'MO', 'NOC', 'REGN', 'EL', 'PGR', 'BKNG', 'DUK', 'TGT', 'SLB', 'SO'
                   ]

Test_stock_list = ['AMZN', 'TSLA', 'MSFT','GOOG', 'XOM']
# # wkly_dataset_path = '/cpr_backtest/com/xxxx/narrowCPR/'
# wkly_from_date = '2019-12-30'
# wkly_to_date = '2022-10-30'
