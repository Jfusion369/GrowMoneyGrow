# my webscraping program to check the stock price
    
    

#Im using imported modules to webscrape  stock qoutes.

""" 
("I commented out this section of code when I moved it to the StockLib.py file. then I imported Stocklib for cleaner code")
from datetime  import datetime as dt, timedelta as td
import matplotlib.pyplot as plt
from matplotlib import style
import pandas 
import pandas_datareader.data as web
import yfinance as yf """
import StockLib

""" ("I created a 'counter' variable and set it 10. Then set a while/ except loop to prompt user input for ticker symbol or quit.  the countrt should increase by 1 after each input")
I stated with a {while 1==1:] loop to be able to run the program and then added the var counter and except to be able to run and not crash the program if a invalid input was entered"""

counter = 0
while counter  < 10:
    try:
        tickersymbol = input("Enter ticker symbol : " )
        if tickersymbol == "quit":
            break

        df = StockLib.GetQuote(tickersymbol)
        #start = dt.now() + td(days=-7)
        #end = dt.now()
        #df = web.DataReader(tickersymbol, 'yahoo', start, end)
        #df.reset_index(inplace=True)
        #df.set_index("Date", inplace=True)

        print(df.head())
        counter += 1
     #the except was to make sure a valid ticker symbol 
     #was inputed and if not the output would alert invalid ticker symbolol
    except:
        print('Invaid ticker symbool '  + tickersymbol)
