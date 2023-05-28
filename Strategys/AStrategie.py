from abc import ABC, abstractmethod
import pandas as pd

class Strategie(ABC):
    def __init__(self, period):
        self._indicators = {}
        self._StopLoss = 0
        self._TakeProfit = 0
        self._period = period

    def addIndicator(self, name, indicator):
        self._indicators[name] = indicator

    def getIndicator(self, name):
        return self._indicators.get(name)

    def getIndicators(self):
        return self._indicators

    def getPeriod(self):
        return self._period

    def update(self, OHLCV):
        for indicator in self._indicators.values():
            indicator.update(OHLCV)

    def addStopLoss(self, stopLoss):
        self._StopLoss = stopLoss

    def addStopLoss(self, value, pourcent):
        valuePourcent = (pourcent * float(value) / 100.0)
        self._StopLoss = float(value) - valuePourcent

    def manageStopLoss(self, value, pourcent):
        valuePourcent = (pourcent * float(value) / 100)
        targetStopLoss = float(value) - valuePourcent

        if targetStopLoss > self._StopLoss:
            self._StopLoss = targetStopLoss

    def getStopLoss(self):
        return self._StopLoss

    def addTakeProfit(self, takeProfit):
        self._TakeProfit = takeProfit

    def getTakeProfit(self):
        return self._TakeProfit

    @abstractmethod
    def execute(self, OHLCV):
        pass
