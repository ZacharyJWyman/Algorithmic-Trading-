#we want to predict if stock went up or down for the day

#idea: want to predict whether the stock on a monday will be up on friday

import pandas_datareader.data as web
import datetime
import pandas as pd

tickers = ['MSFT', 'FB', 'AMZN', 'GOOGL', 'TSLA', 'V', 'NKE']

start_date = '2012-08-04'
end_date = '2020-10-08'


df = web.DataReader(tickers, 'yahoo', start_date, end_date)
df = df[['Open', 'Close']]
df.index = df.index.dayofweek
df.to_csv(r'C:\Users\19712\OneDrive\Desktop\alpaca\stocks\train.csv')