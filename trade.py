from config import *
from main_script import *
import yfinance as yf
import time

#stocks to watch
tickers = ['MSFT', 'AAPL', 'AMZN', 'FB', 'GOOG']
CLOCK = clock()
MARKET_OPEN = CLOCK['next_open'] #need to specify script to trade between these times
MARKET_CLOSE = CLOCK['next_close']

#below line will integrate clock into script. remove # when ready.
#if CLOCK['is_open'] is True: #specifies if market is open
#else: 
    #print('market is open at: ' + str(CLOCK['next_open']))
while True:

#order = create_order('MSFT', 1, 'buy', 'market', 'day')

    #request price every minute on MSFT (2000 requests per hour = 33 requests per min)
    MSFT = yf.Ticker('MSFT')
    print('Ask Price:' + str(MSFT.info['ask']))
    print('NEW REQUEST')
    time.sleep(3)

    



    #makes trade every 10 seconds until script is canceled #ctrl c
    order = create_order('MSFT', 1, 'buy', 'market', 'day')
    time.sleep(10)
    print('Trade Confirmed')
    

    
    


