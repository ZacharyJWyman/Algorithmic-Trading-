#we want to predict if stock went up or down for the day

#idea: want to predict whether the stock on a monday will be up on friday

import pandas_datareader.data as web
import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

tickers = 'MSFT'

start_date = '2012-08-04'
end_date = '2020-10-08'


df = web.DataReader(tickers, 'yahoo', start_date, end_date)
df = df['Close']
df.index = df.index.dayofweek
df.to_csv(r'C:\Users\19712\OneDrive\Desktop\alpaca\stocks\train.csv')
#%%
percent = int(np.round(len(df) *.8))
train = df[:percent]
test = df[percent:]

#%%
smooth_window = 2500
scaler = MinMaxScaler()
train = train.values.reshape(-1,1)
test = test.values.reshape(-1,1)
for d in range(0,10000, smooth_window):
    scaler.fit(train[d:d+smooth_window, :])
    train[d:d+smooth_window,:] = scaler.transform(train[d:d+smooth_window,:])

scaler.fit(train[d+smooth_window:,:])
train[d+smooth_window:,:] = scaler.transform(train[d+smooth_window:,:])

train = train.reshape(-1)
test = scaler.transform(test).reshape(-1)