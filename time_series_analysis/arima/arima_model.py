import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv', index_col = 'Month')

airline.head()
airline.tail()
airline.describe()
airline.info()

# remove missing values 
airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)
airline.head()

from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(airline['Thousands of Passengers'], 
                            model = 'multiplicative')
result.plot()
