from Indicators.AIndicator import Indicator
import pandas as pd

def EMA(data, column, time_period):
    EMA = data[column].ewm(span=time_period, adjust=False).mean()

    return EMA

class Trendline(Indicator):
    def __init__(self, column, pourcent, timeFast, timeSlow):
        super().__init__(column)
        self.pourcent = pourcent
        self.timeFast = timeFast
        self.timeSlow = timeSlow

    def update(self, data):
        super().update(data)

    def calculate(self):
        fastEMA = EMA(self.data, self.column, self.timeFast).iloc[-1]
        slowEMA = EMA(self.data, self.column, self.timeSlow).iloc[-1]
        valuePourcent = self.pourcent * fastEMA / 100

        if (fastEMA - slowEMA) <= valuePourcent and (fastEMA - slowEMA) >= 0:
            return "trendLine"
        elif fastEMA > slowEMA:
            return "uptrend"
        else:
            return "downtrend"
