from Strategys.AStrategie import Strategie
from Indicators.BBIndicator import BB

class BBStrategy(Strategie):
    def __init__(self, bbPeriod):
        super().__init__(bbPeriod)
        self.addIndicator("BB", BB("Close", bbPeriod))

    def execute(self, OHLCV):
        self.update(OHLCV)
        upperBand, lowerBand = self.getIndicator("BB").calculate()
        if OHLCV["Close"].iloc[-1] > upperBand.iloc[-1]:
            return "BUY"
        elif OHLCV["Close"].iloc[-1] < lowerBand.iloc[-1]:
            return "SELL"
        else:
            return "HOLD"