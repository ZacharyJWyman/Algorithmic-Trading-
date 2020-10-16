from config import *
from main_script import *
import yfinance as yf
import time
import schedule
from collections import defaultdict

#stocks to watch
tickers = ['MSFT', 'AAPL', 'AMZN', 'FB', 'GOOG']

#CONSTS
CLOCK = clock()
MARKET_OPEN = CLOCK['next_open'] #need to specify script to trade between these times
MARKET_CLOSE = CLOCK['next_close']
PRICE = 0
stock_dict = defaultdict(list)


#below line will integrate clock into script. remove # when ready.
while CLOCK['is_open'] is False: #specifies if market is open
    
    #code for first time append 0 to stock price
        

    for tick in tickers:
        #request price every minute on MSFT (2000 requests per hour = 33 requests per min)
        obj = yf.Ticker(tick)
        price = obj.info['ask']
        stock = obj.info['symbol']
        print('Ask Price:' + str(price))
        time.sleep(1)


        if price > stock_dict[stock][-1]: #if next ping greater than prior ping
            order = create_order(tick, 1, 'buy', 'market', 'day')
            print('Trade Confirmed')
            time.sleep(1)
        else:
            print('Price Decreased: No trade made')

        #append price to end of dict
        stock_dict[stock].append(price)
        
else: 
    print('market is open at: ' + str(CLOCK['next_open']))
    
    


