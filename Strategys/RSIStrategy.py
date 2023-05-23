from Strategys.AStrategie import Strategie
from Indicators.RSIIndicator import RSI

class RSIStrategy(Strategie):
    def __init__(self, rsiPeriod, overBought, overSold):
        super().__init__(rsiPeriod)
        self._overBought = overBought
        self._overSold = overSold
        self.addIndicator("RSI", RSI("Close", rsiPeriod))

    def execute(self, OHLCV):
        self.update(OHLCV)
        rsi = self.getIndicator("RSI").calculate().iloc[-1]
        if rsi > self._overBought:
            return "BUY"
        elif rsi < self._overSold:
            return "SELL"
        else:
            return "HOLD"