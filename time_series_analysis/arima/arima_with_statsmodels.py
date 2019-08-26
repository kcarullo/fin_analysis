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

from statsmodels.tsa.stattools import adfuller
result = adfuller(df['Milk in Pounds per Cow'])

def adf_check(time_series):
    result = adfuller(time_series)
    print(" Augmented Dicky-Fuller Test")
    labels = ['ADF Test Statistic', 'p-value', '# of lags', 
              'Num of Observations used']
    
    for value, label in zip(result, labels):
        print(label+ " : "+str(value))
        
    if result[1] <= 0.05:
        print("Strong evidence against null hypothesis")
        print("Reject null hypothesis")
        print("Data has no unit root and is stationary")
    else:
        print("Weak evidence against null hypothesis")
        print("Fail to reject null hypothesis")
        print("Data has a unit root, it is non-stationary")

adf_check(time_series)
        
df['First Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(1)
df['First Difference'].plot()
    
adf_check(df['First Difference'].dropna())

df['Milk Second Difference'] = df['First Difference'] - df['First Difference'].shift(1)
adf_check(df['Milk Second Difference'].dropna())
df['First Difference'].plot()

df['Seasonal Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(12)
df['Seasonal Difference'].plot()
adf_check(df['Seasonal Difference'].dropna())

df['Seasonal First Difference'] = df['First Difference'] - df['First Difference'].shift(12)
df['Seasonal First Difference'].plot()
adf_check(df['Seasonal First Difference'].dropna())

# Auto Correlation Plots 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
fig_first = plot_acf(df['First Difference'].dropna())
fig_seasonal_first = plot_acf(df['Seasonal First Difference'].dropna())

#pacf
fig_seasonal_pacf = plot_pacf(df['Seasonal First Difference'].dropna(),
                              method='ywmle')

# autocorrelation with pandas 
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df['Seasonal First Difference'].dropna())

plot_acf(df['Seasonal First Difference'].dropna())
plot_pacf(df['Seasonal First Difference'].dropna(), method='ywmle')

# implementing ARIMA model
from statsmodels.tsa.arima_model import ARIMA
model = sm.tsa.statespace.SARIMAX(df['Milk in Pounds per Cow'], order=(0,1,0),
                                  seasonal_order=(1,1,1,12))
results = model.fit()
print(results.summary())
results.resid
results.resid.plot()
results.resid.plot(kind='kde')

df['forecast'] = results.predict(start=150, end=168)
df[['Milk in Pounds per Cow', 'forecast']].plot(figsize=(12,8))

# add future rows so we can forecast for the future months
from pandas.tseries.offsets import DateOffset
# df.index[-1] is the last month in the index col you add a offset where months
# is equal to x. The for loop is going to add the offset 1 month, 2, 3 and so on
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(1,24)]
future_dates
future_df = pd.DataFrame(index=future_dates, columns=df.columns)
final_df = pd.concat([df, future_df])
final_df.tail()

final_df['forecast'] = results.predict(start=168, end=192)
final_df.tail()

final_df[['Milk in Pounds per Cow', 'forecast']].plot(figsize=(12,8))
