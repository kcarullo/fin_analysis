import numpy as np 
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt 

df = pd.read_csv('monthly-milk-production-pounds-p.csv')
df.head()

# rename the columns
df.columns = ['Month', 'Milk in Pounds per Cow']
df.head()

df.tail()

#drop row 168  Monthly milk production: pounds per cow. Jan 6...
df.drop(168, axis=0, inplace=True)
df.tail()

# convert the month column to a date time column
df['Month'] = pd.to_datetime(df['Month'])

# set the index to the month col
df.set_index('Month', inplace=True)
df.head()

df.index

df.describe().transpose()

# visualize the data
df.plot()

time_series = df['Milk in Pounds per Cow']
type(time_series)

time_series.rolling(12).mean().plot(label='12 Month Rolling Mean')
time_series.rolling(12).std().plot(label='12 Month Rolling Std')
time_series.plot()
plt.legend()

from statsmodels.tsa.seasonal import seasonal_decompose
decomp = seasonal_decompose(time_series)
decomp.plot()
