import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data
df.describe()

# additional information about the columns 
print(sm.datasets.macrodata.NOTE)

df.head()

# set the year to be a time series index instead of a column
index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))

df.index = index

df.head()

df['realgdp'].plot()

gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])
df['trend'] = gdp_trend

df[['realgdp', 'trend']].plot()

# zoom in on 2000-03-31 to the last date avaliable 
df[['realgdp', 'trend']]['2000-03-31':].plot()
