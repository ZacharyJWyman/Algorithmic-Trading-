import requests, json

API_KEY = 'PKUEFF2VVYWWI7AR4CXG'
SECRET_KEY = 'q3uCJkpcOxgzHDHVABFHzlWMOHLSrDU3ZrGtuyw8'
BASE_URL = 'https://paper-api.alpaca.markets'
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#make requests
def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)

    return json.loads(r.content)

#   create order(ticker, qty, buy/sell, market/limit, day)
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

test_order = create_order('MSFT', 10, 'buy', 'market', 'day')

