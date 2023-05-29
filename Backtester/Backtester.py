import mplfinance as mpf
import pandas as pd

def convert_columns_to_numeric(dataframe, columns):
    for column in columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
    return dataframe

class Backtester():
    def __init__(self, OHLCV):
        self.buySignals = []
        self.sellSignals = []
        self.indicatorValues = {}
        self.OHLCV = OHLCV

    def addBuySignal(self, index, value):
        self.buySignals.append((index, value))

    def addSellSignal(self, index, value):
        self.sellSignals.append((index, value))

    def addIndicatorValue(self, indicator, index, value):
        if indicator not in self.indicatorValues:
            self.indicatorValues[indicator] = []
        self.indicatorValues[indicator].append(value)

    def getBuySellSignals(self):
        filtered_buy_signals = list(filter(lambda x: x[1] is not None, self.buySignals))
        filtered_sell_signals = list(filter(lambda x: x[1] is not None, self.sellSignals))

        buySignals = pd.DataFrame(filtered_buy_signals, columns=['Date', 'Value'])
        buySignals.set_index('Date', inplace=True)
        buySignals.columns = ['Buy']

        sellSignals = pd.DataFrame(filtered_sell_signals, columns=['Date', 'Value'])
        sellSignals.set_index('Date', inplace=True)
        sellSignals.columns = ['Sell']

        return [buySignals, sellSignals]

    def plotStrategy(self):
        self.OHLCV.index = pd.to_datetime(self.OHLCV.index, unit='m')

        columns_to_convert = ['Open', 'High', 'Low', 'Close', 'Volume']
        self.OHLCV = convert_columns_to_numeric(self.OHLCV, columns_to_convert)

        custom_marketcolors = mpf.make_marketcolors(
            up='g', down='r',
            wick={'up': 'g', 'down': 'r'},
            edge={'up': 'g', 'down': 'r'},
            volume='inherit'
        )

        custom_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=custom_marketcolors)

        buy_markers = [self.OHLCV["Close"].iloc[i] if i in [x for x, _ in self.buySignals] else float('nan') for i in range(len(self.OHLCV))]
        sell_markers = [self.OHLCV["Close"].iloc[i] if i in [x for x, _ in self.sellSignals] else float('nan') for i in range(len(self.OHLCV))]

        if not self.buySignals and not self.sellSignals:
            print("No buy or sell signals")
            mpf.plot(self.OHLCV, type='candle', style=custom_style, volume=True, title='Backtest', ylabel='Price', ylabel_lower='Volume')
            return

        indicator_plots = []
        for indicator, values in self.indicatorValues.items():
            if values:
                if isinstance(values[0], tuple):
                    for idx, value_name in enumerate(['Upper', 'Lower']):
                        value_data = [value[idx] for value in values]
                        indicator_df = pd.DataFrame(value_data, columns=['Value'])
                        indicator_df['Date'] = self.OHLCV.index
                        indicator_df.set_index('Date', inplace=True)
                        indicator_plots.append(mpf.make_addplot(indicator_df, panel=0, ylabel=f'{indicator} {value_name}', secondary_y=True))
                else:
                    indicator_df = pd.DataFrame(values, columns=['Value'])
                    indicator_df['Date'] = self.OHLCV.index
                    indicator_df.set_index('Date', inplace=True)
                    indicator_plots.append(mpf.make_addplot(indicator_df, panel=0, ylabel=indicator, secondary_y=True))

        signals = [mpf.make_addplot(buy_markers, scatter=True, markersize=100, marker='^', color='g', panel=0),
                mpf.make_addplot(sell_markers, scatter=True, markersize=100, marker='v', color='r', panel=0)]

        plots = signals + indicator_plots

        mpf.plot(self.OHLCV, type='candle', addplot=plots, style=custom_style, volume=True, title='Multi-Indicator Strategy', ylabel='Price', figscale=1.5)
