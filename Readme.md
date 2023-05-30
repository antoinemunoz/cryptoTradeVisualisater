hi This is my personal project for Epitech where you can use a tool to visualize your crypto strategy. Here are the steps to implement it in Python:

Step 1: Install Requirements

Install the necessary Python packages:

    Download and install Python.
    Download and install pip (Python package manager).
    Install the necessary libraries with pip:

pip install python-binance pandas matplotlib abcmeta

Step 2: Create a Binance Account and API

    Sign up for a Binance account.
    Click on your profile.
    Go to 'API Management'.
    Click on 'Create API'.
    Adjust the restrictions:
        Enable 'Allow Universal Transfers'.
        Enable 'Enable Spot and Margin Trading'.
        Enable 'Allow Reading'.

Step 3: Integrate the Binance API with the Program

Navigate to the Binance directory and create a Config.py file:

cd Binance
touch Config.py
nano Config.py

In Config.py, add your Binance API credentials:

config = {
    'api_key': 'your_api_key',
    'api_secret': 'your_api_secret',
}

Step 4: Create an Indicator

Go to the Indicators directory and create a new Python file:

cd Indicators
touch NameIndicator.py

Add the following code to the top of your file:

from Indicators.AIndicator import Indicator
import pandas as pd

Create a new class that inherits from Indicator and add your logic in the calculate method.

class NameIndicators(Indicator):
    def __init__(self, column, time_period=20):
        super().__init__(column, time_period)

    def update(self, data):
        super().update(data)

    def calculate(self):
        # Implement your logic here

Step 5: Create a Strategy

Navigate to the Strategys directory and create a new Python file:

bash

cd Strategys
touch NameStrategy.py

Add the following code to the top of the file:

from Strategys.AStrategie import Strategie
from Indicators.NameIndicator import NameIndicator

Replace NameIndicator with the name of your indicator. Then create a new class that inherits from Strategie and implements your strategy.

class NameStrategy(Strategie):
    def __init__(self, bbPeriod):
        super().__init__(bbPeriod)
        self.addIndicator("BB", BB("Close", bbPeriod))

    def execute(self, OHLCV):
        # Implement your strategy here

Step 6: Add Your Strategy to the Main Program

Include your strategy in the main Python file:

from Strategys.NameStrategy import NameStrategy

Replace NameStrategy with the name of your strategy and replace the existing strategy line:

strategy = RSIStrategy(14, 70, 30)
by
strategy = NameStrategy(20)

Step 7: Download the Data

Use the provided script to download the data:

python3 OHLCV.py SYMBOL LIMIT INTERVAL

For example:

python3 OHLCV.py BTCUSDT 1000 min

Step 8: Run the Backtest

You can now run the backtest:

python3 main.py OHLCVBTCUSDT1000min.csv

Replace OHLCVBTCUSDT1000min.csv with the name of your data file.

Step 9: Enjoy the Results

You can view the results in the results folder. Happy trading!