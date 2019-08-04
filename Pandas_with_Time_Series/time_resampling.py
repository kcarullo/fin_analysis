import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('walmart_stock.csv', index_col = 'Date', parse_dates = True)

df.head()
df.info()
# convert Date column to datetime64[ns] instead of an object
#df['Date'] = pd.to_datetime(df['Date'])
# this accomplishes the same goal as directly above 
# df['Date'] = df['Date'].apply(pd.to_datetime)
#df.set_index('Date', inplace=True)
#df

#yearly 
df.resample(rule = 'A').mean()
# quarterly
df.resample(rule = 'Q').mean()
# max 
df.resample(rule = 'A').max()

#custom function 
def first_day(entry):
    return entry[0]

df.resample('A').apply(first_day)

df['Close'].resample('M').mean().plot(kind = 'bar', figsize = (16, 6), rot = 45)