from Binance.BinanceClass import binanceClass
from Binance.Config import config
import sys

def main(symbol, limit, interval):
    binance = binanceClass(config['api_key'], config['api_secret'])
    OHLCV = binance.getOHLCV(symbol, limit, interval)
    OHLCV.to_csv("OHLCV" + symbol + str(limit) + interval + ".csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py SYMBOL LIMIT INTERVAL")
        sys.exit(1)

    symbol = sys.argv[1]
    limit = int(sys.argv[2])
    interval = sys.argv[3]

    main(symbol, limit, interval)
