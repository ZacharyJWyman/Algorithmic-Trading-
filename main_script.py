import config
import requests, json

API_KEY = config.API_KEY
SECRET_KEY = config.SECRET_KEY
BASE_URL = 'https://paper-api.alpaca.markets'
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
WATCHLIST_URL = '{}/v2/watchlists'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#make requests
def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)

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
