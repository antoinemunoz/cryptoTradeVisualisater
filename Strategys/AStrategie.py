from abc import ABC, abstractmethod
import pandas as pd

class Strategie(ABC):
    def __init__(self, period):
        self._indicators = {}
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

    @abstractmethod
    def execute(self, OHLCV):
        pass
