from Strategys.BBStrategy import BBStrategy
from Strategys.RSIStrategy import RSIStrategy
from Strategys.ExoStrategie import ExoStrategie

import sys
import pandas as pd

def main(OHLCV):
    # strategy = BBStrategy(20)
    # strategy = RSIStrategy(14, 70, 30)
    strategy = ExoStrategie(0.18, 20, 40, 20)
    stableCoins = 1000
    tradingCoins = 0
    gross_profit = 0
    gross_loss = 0

    for i in range(len(OHLCV)):
        state = strategy.execute(OHLCV[:strategy.getPeriod() + i])

        if state == "BUY" and stableCoins > 15:
            tradingCoins = stableCoins / OHLCV["Close"].iloc[i]
            stableCoins = 0
        elif state == "SELL" and tradingCoins > 0.01:
            stableCoins = tradingCoins * OHLCV["Close"].iloc[i]
            tradingCoins = 0

    print("Stable coins: " + str(stableCoins))
    print("Trading coins: " + str(tradingCoins))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py OHLCV.csv")
        sys.exit(84)

    OHLCV = pd.read_csv(sys.argv[1])
    main(OHLCV)

