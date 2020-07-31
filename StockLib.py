""" I setup a secondary py file to seperate the code for  easier reading 
I also changed my start and end date to return the last 7 days of market analysis instead of the first of the year like in my previopus code  """ 

from datetime  import datetime as dt, timedelta as td
import matplotlib.pyplot as plt
from matplotlib import style
import pandas 
import pandas_datareader.data as web
import yfinance as yf


def GetQuote(tickersymbol):
    style.use('ggplot')
    start = dt.now() + td(days=-7)
    end = dt.now()
    df = web.DataReader(tickersymbol, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    return df