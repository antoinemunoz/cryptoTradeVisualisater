from Strategys.AStrategie import Strategie
from Indicators.TrendlineIndicator import Trendline
from Indicators.BBIndicator import BB

class ExoStrategie(Strategie):
    def __init__(self, pourcent, timeFast, timeSlow, bbPeriod=20):
        super().__init__(timeSlow)
        self.addIndicator("BB", BB("Close", bbPeriod))
        self.addIndicator("Trendline", Trendline("Close", pourcent, timeFast, timeSlow))
        self.state = "Reloading"

    def execute(self, OHLCV):
        self.update(OHLCV)
        trend = self.getIndicator("Trendline").calculate()
        BBuper, BBdown = self.getIndicator("BB").calculate()

        if trend == "uptrend":
            if self.statue == "Charging" and float(OHLCV["Close"].iloc[-1]) > float(BBuper.iloc[-1]):
                self.addStopLoss(OHLCV["Close"].iloc[-1], 0.1)
                self.statue = "Take Profit"
                return "BUY"
            elif self.statue == "Take Profit":
                self.manageStopLoss(OHLCV["Close"].iloc[-1], 0.1)
        elif trend == "trendLine":
            self.statue = "Charging"
        elif trend == "downtrend":
            return "SELL"
            self.addStopLoss(0)
            self.statue = "Reloading"

        if float(OHLCV["Close"].iloc[-1]) < self.getStopLoss():
            self.statue = "Reloading"
            return "SELL"

        return "HOLD"