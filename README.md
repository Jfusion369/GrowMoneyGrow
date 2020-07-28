# GrowMoneyGrow

# a program for checking 10 or less stocks tickers for the last 5-7 days of trading information

## User interface:
1. run the pogram in the terminal
  ```
  pip install -r requirements.txt
  python stock.py
  ```
2. enter any valid Stock ticker symbol to recieve the last 5 buisness days of high/low open/ close information
  > Examples: A, AAPL, BRK.A, C, GOOG, HOG, HPQ, INTC, KO, LUV, MMM, MSFT, T, TGT, TXN, WMT
   ```
   Enter ticker symbol : AAPL
   ```
   
   Results:
   ```
                     High         Low  ...    Volume   Adj Close
   Date                                ...
   2020-07-21  397.000000  386.970001  ...  25911500  388.000000
   2020-07-22  391.899994  386.410004  ...  22250400  389.089996
   2020-07-23  388.309998  368.040009  ...  49251100  371.380005
   2020-07-24  371.880005  356.579987  ...  46323800  370.459991
   2020-07-27  379.619995  373.927490  ...  28830631  379.239990

   ```
3. I have limted the amount of stocks you can check to 10 where it will end the program after
4. If 10 is too many stocks to check the user can end the program by typing 
  ```
  quit
  ```
5. If a invalid entry is entered the program will return 'invalid ticker symbol' and allow the user to retry
