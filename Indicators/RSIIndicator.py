from Indicators.AIndicator import Indicator
import pandas as pd

class RSI(Indicator):
    def __init__(self, column, time_period=14):
        super().__init__(column, time_period)

    def update(self, data):
        super().update(data)

    def calculate(self):
        numeric_data = pd.to_numeric(self.data[self.column], errors='coerce')

        delta = numeric_data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=self.time_period).mean()
        avg_loss = loss.rolling(window=self.time_period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi
