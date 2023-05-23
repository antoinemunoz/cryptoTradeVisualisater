from abc import ABC, abstractmethod
import pandas as pd

class Indicator(ABC):
    def __init__(self, column, time_period=None):
        self.column = column
        self.data = pd.DataFrame()
        self.time_period = time_period

    def update(self, data):
        self.data = pd.concat([self.data, data], ignore_index=True)

    @abstractmethod
    def calculate(self):
        pass