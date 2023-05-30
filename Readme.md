Hi this is my personal project for epitech, where you can use a tools for visualizing your crypto strategy, but you need it to implement it on python.

For doing it:

1: install requirement

download python
download pyp
pip install python-binance
pip install pandas
pip install matplotlib
pip install abcmeta

after you download this following requierement, you need to create a binance api

For doing it

2: create binance acount
click to your profil
->Gestion api
->Créer api
->Modifier les restrictions
->activer "Permet les transferts universels"
->activer "Activer le trading Spot et sur marge"
->activer "Permetre la lecture"

Nice you created you binance api, now you can integrate it to the program

3: integrate it to the program

cd Binance
touch Config.py
nano Config.py

config = {
    'api_key': your api key,
    'api_secret': your api secret,
}

Now that you integrate it the program, is time to create your first indicator, where you can see the abstrat, (template for doing your indicators), now that you have see how its work, we gonna go step by step for doing it.

4: create indicators

cd Indicators
touch NameIndicator.py

past this to the top of the file
from Indicators.AIndicator import Indicator
import pandas as pd

create the class
making inerate from indicator
ex:
class BB(Indicator):
    def __init__(self, column, time_period=20):
        super().__init__(column, time_period)

    def update(self, data):
        super().update(data)

this two fonctions are juste exemple, if you want to change it, do it!
now integrate the logic of your class on the def calculate(self):

Nice, you create your firt indicator, now you can try to create a strategy, quite the same like the indicators but there is some little detail to change

5: create your strategy

cd Strategys
touch NameStrategy.py

past this to the top of the file

from Strategys.AStrategie import Strategie
from Indicators.NameIndicator import NameIndicator

remplace NameIndicator by the name of your indicator

create the class
making inerate from Strategie
ex:
class BBStrategy(Strategie):
    def __init__(self, bbPeriod):
        super().__init__(bbPeriod)
        self.addIndicator("BB", BB("Close", bbPeriod))

integrating the logic of your class on the def execute(self, OHLCV):

Nice, you create your firt strategy, now you can try to add it to the main for backtesting it

6: add your strategy to the main

include your strategy to the main
ex:
from Strategys.NameStrategy import NameStrategy
remplace NameStrategy by the name of your strategy

add your strategy to the main by remplacing this line
strategy = RSIStrategy(14, 70, 30)
by
strategy = NameStrategy(20)

now that you implemented it, time to lunch it,

but before it you need to download the data

7: download the data

python3 OHLCV.py SYMBOL LIMIT INTERVAL
for ex:
python3 OHLCV.py BTCUSDT 1000 min

now you can lunch the backtest by doing
python3 main.py OHLCVBTCUSDT1000min.csv
or the name of your csv

8: enjoy

you can see the result on the result folder
