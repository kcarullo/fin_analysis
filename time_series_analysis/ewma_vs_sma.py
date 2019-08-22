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

# create 6 month moving avg
airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()

# create a 12 moving avg
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot(figsize=(10,8))

# EWMA exponetially weighted moving average
airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline[['Thousands of Passengers', 'EWMA-12']].plot(figsize=(10,8))
