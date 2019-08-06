# Import the libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader
import datetime
import pandas_datareader.data as web

#prepare the data
start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

tesla = web.DataReader('TSLA', 'yahoo', start,end)
tesla.head()

ford = web.DataReader('F', 'yahoo', start,end)
ford.head()

gm = web.DataReader('GM', 'yahoo', start,end)
gm.head()

# Visualizing the opening prices
tesla['Open'].plot(label='Tesla',figsize=(12,8),title='Opening Prices')
ford['Open'].plot(label='Ford')
gm['Open'].plot(label='GM')
plt.legend()

# Visualizing Volume Traded
tesla['Volume'].plot(label='Tesla',figsize=(12,8),title='Volume Traded')
ford['Volume'].plot(label='Ford')
gm['Volume'].plot(label='GM')
plt.legend()

# Find the date for the maximum trading folume for Ford. 
ford['Volume'].idxmax() # 2013-12-18 00:00:00

