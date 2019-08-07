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

# Candle stick chart for Ford in Jan 2012
#!/usr/bin/env python
from matplotlib.dates import DateFormatter,date2num,WeekdayLocator,DayLocator,MONDAY
from mpl_finance import candlestick_ohlc

# puts an index column back into the dataframe
ford_rest = ford.loc['2012-01'].reset_index()
ford_rest.head()

ford_rest['date_ax'] = ford_rest['Date'].apply(lambda date: date2num(date))
ford_rest.head()

list_of_cols = ['date_ax', 'Open', 'High', 'Low', 'Close']
ford_values = [tuple(vals) for vals in ford_rest[list_of_cols].values ]

ford_values

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

candlestick_ohlc(ax,ford_values,width=0.6,colorup='g',colordown='r')

# Daily Percent Change rt = (Pt / Pt-1 ) - 1 ### t stands for time 
# Two methods to of how to do this
# Method 1
tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1)) - 1
# Method 2
tesla['returns'] = tesla['Close'].pct_change(1)
#tesla['returns'].head()
gm['returns'] = gm['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)

tesla['returns'].hist(bins=100,label='Tesla',figsize=(10,8),alpha=0.4)
gm['returns'].hist(bins=100,label='GM',figsize=(10,8),alpha=0.4)
ford['returns'].hist(bins=100,label='Ford',figsize=(10,8),alpha=0.4)
plt.title('Histogram of Daily Percent Change')
plt.legend()

# Daily return KDE plot

tesla['returns'].plot(kind='kde',label='Tesla',figsize=(10,8))
gm['returns'].plot(kind='kde',label='GM',figsize=(10,8))
ford['returns'].plot(kind='kde',label='Ford',figsize=(10,8))
plt.title('KDE Plot of Daily Percent Change')
plt.legend()
# Daily return box plot
box_df = pd.concat([tesla['returns'],ford['returns'],gm['returns']],axis=1)
box_df.columns = ['Tesla', 'Ford', 'GM']
box_df.plot(kind='box',figsize=(8,11))

# scatter matrix daily return 
from matplotlib.ticker import FormatStrFormatter
s_matrix = scatter_matrix(box_df,figsize=(8,8),alpha=0.2,hist_kwds={'bins':100},range_padding=0.06)
for axs in s_matrix[:,0]:
    axs.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    
# ford and gm appear to have a relationship
box_df.plot(kind='scatter', x='Ford',y='GM',alpha=0.5,figsize=(8,8))

# cumulative daily returns 

tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()
ford['Cumulative Return'] = (1 + ford['returns']).cumprod()
gm['Cumulative Return'] = (1 + gm['returns']).cumprod()

tesla['Cumulative Return'].plot(label='Tesla',figsize=(16,8))    
ford['Cumulative Return'].plot(label='Ford')
gm['Cumulative Return'].plot(label='GM')
plt.title('Cumulative Returns')
plt.legend()

# cumulative return between ford and gm
ford['Cumulative Return'].plot(label='Ford',figsize=(16,8))
gm['Cumulative Return'].plot(label='GM')
plt.title('Cumulative Returns Ford v GM')
plt.legend()

