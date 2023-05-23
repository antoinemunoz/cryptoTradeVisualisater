from Indicators.AIndicator import Indicator
import pandas as pd

class BB(Indicator):
    def __init__(self, column, time_period=20):
        super().__init__(column, time_period)

    def update(self, data):
        super().update(data)

    def calculate(self):
        MA = self.data[self.column].rolling(window=self.time_period).mean()
        SD = self.data[self.column].rolling(window=self.time_period).std()
        upperBand = MA + (SD * 2)
        lowerBand = MA - (SD * 2)

        return upperBand, lowerBand
