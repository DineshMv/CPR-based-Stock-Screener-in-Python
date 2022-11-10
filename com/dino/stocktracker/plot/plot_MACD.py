from com.dino.stocktracker.indicators.MACD import *

fb_green = dict(y1=macd.values, y2=signal.values, where=signal < macd, color="#93c47d", alpha=0.5, interpolate=True)
fb_red = dict(y1=macd.values, y2=signal.values, where=signal > macd, color="#e06666", alpha=0.5, interpolate=True)
fb_green['panel'] = 1
fb_red['panel'] = 1
fb = [fb_green, fb_red]

apds = [mpf.make_addplot(exp12, color='red', width=0.5),
        mpf.make_addplot(exp26, color='c', width=0.5),
        mpf.make_addplot(histogram, type='bar', width=0.5, panel=1, color='dimgray', alpha=1, secondary_y=True),
        mpf.make_addplot(macd, panel=1, width=0.5, color='fuchsia', secondary_y=False),
        mpf.make_addplot(signal, panel=1, width=0.5, color='b', secondary_y=False)
        ]

s = mpf.make_mpf_style(base_mpf_style='yahoo', rc={'figure.facecolor': 'lightgray'})

mpf.plot(df, type='candle', addplot=apds, figscale=2, figratio=(6, 5), title='\n\nMACD',
         style=s, volume=True, volume_panel=2, panel_ratios=(5, 2, 1), fill_between=fb)  # , show_nontrading=True)
