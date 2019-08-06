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

# show total traded which is the open price * by the volume traded
tesla['Total Traded'] = tesla['Open']*tesla['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']

tesla['Total Traded'].plot(label='Tesla',figsize=(16,8))
ford['Total Traded'].plot(label='Ford')
gm['Total Traded'].plot(label='GM')
plt.title('Total Traded')
plt.legend()
# find the date of the spike in tesla trading 
tesla['Total Traded'].idxmax() # ('2014-02-25 00:00:00')

# Plot the Moving Averages MA, specifically MA50 and MA200 for GM
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open', 'MA50', 'MA200']].plot(figsize=(16,8))

# Scatter matrix between tesla, ford, gm
from pandas.plotting import scatter_matrix
car_comp = pd.concat([tesla['Open'],gm['Open'],ford['Open']], axis=1)

car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']
car_comp.head()
scatter_matrix(car_comp,figsize=(16,6), alpha=0.2,hist_kwds={'bins':50})
