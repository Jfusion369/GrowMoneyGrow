#Im using imported modules to webscrape Tesla stock qoutes.

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas 
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()
df = web.datareader("TSLA", 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())
