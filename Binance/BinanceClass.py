from binance.client import Client
from datetime import datetime
import pandas as pd
import math

def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def writeFile(filename, lines):
    with open(filename, "a") as file:
        file.write("\n" + lines)

class binanceClass:
    def __init__(self, key, secret):
        self.client = Client(key, secret)

    def getBalance(self, coin):
        info = self.client.get_account()
        df = pd.DataFrame(info["balances"])

        if df.loc[df['asset'] == coin].empty : return 0
        else : return float(df.loc[df['asset'] == coin]['free'])

    def getOHLCV(self, symbol, day, time):
        data = self.client.get_historical_klines(symbol, self.client.KLINE_INTERVAL_5MINUTE, str(day) + " " + time + " ago UTC")

        OHLCV = pd.DataFrame(data)
        OHLCV = OHLCV.rename(columns={0: "Timestamp", 1: "Open", 2: "High", 3: "Low", 4: "Close", 5: "Volume", 6: "CloseTime", 7: "QuoteAssetVolume", 8: "NumberOfTrades", 9: "TakerBuyBaseAssetVolume", 10: "TakerBuyQuoteAssetVolume", 11: "Ignore"})
        OHLCV = OHLCV.drop(columns=["CloseTime", "QuoteAssetVolume", "NumberOfTrades", "TakerBuyBaseAssetVolume", "TakerBuyQuoteAssetVolume", "Ignore"])

        return OHLCV

    def long(self):
        USDT = self.getBalance("USDT")
        eth_price = self.client.get_symbol_ticker(symbol="ETHUSDT")


        if USDT > 15:
            writeFile("log.txt", "go long with " + str(eth_price["price"]) + " at " + str(datetime.now()))
            self.client.order_market_buy(symbol="ETHUSDT", quantity=truncate(USDT / float(eth_price["price"]), 4))

    def short(self):
        eth_price = self.client.get_symbol_ticker(symbol="ETHUSDT")
        ETH = truncate(self.getBalance("ETH"), 4)

        if ETH > 0.01:
            writeFile("log.txt", "go short at " + str(eth_price["price"]) + " at " + str(datetime.now()))
            self.client.order_market_sell(symbol="ETHUSDT", quantity=ETH)