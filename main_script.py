import config
import json
import requests

API_KEY = config.API_KEY
SECRET_KEY = config.SECRET_KEY
BASE_URL = 'https://paper-api.alpaca.markets'
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
WATCHLIST_URL = '{}/v2/watchlists'.format(BASE_URL)
CLOCK_URL = '{}/v2/clock'.format(BASE_URL)
HISTORY_URL = '{}/v2/account/portfolio/history'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}



#make requests
def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)

    return json.loads(r.content)

def clock():

    r = requests.get(CLOCK_URL, headers = HEADERS)
    return json.loads(r.content)



#   create order(ticker, qty, buy/sell, market/limit, day) #sell or buy
def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    
    r = requests.post(ORDERS_URL, json = data, headers = HEADERS)

    return json.loads(r.content)

#watchlists
def get_watchlists():
    r = requests.get(WATCHLIST_URL, headers = HEADERS)

    return json.loads(r.content)

def watchlist(name, symbol):    
    data = {
        'name': name,
        'symbol': symbol
    }

    r = requests.post(WATCHLIST_URL, json = data, headers = HEADERS)

    return json.loads(r.content)

def add_symbol(watchlist_id, symbol):
    data = {
        'symbol': symbol
    }

    r = requests.post(WATCHLIST_URL, json = data, headers = HEADERS)

    return json.loads(r.content)


#FMP Requests (250 per day)
def getROE(stock):
    income_statement =  requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}?period=quarter")
    income_statement = income_statement.json()
    return income_statement

def getHistory():
    r = requests.get(HISTORY_URL, headers = HEADERS)

    return json.loads(r.content)