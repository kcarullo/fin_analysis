import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime 

my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

my_date = datetime(my_year, my_month, my_day)
print(my_date)

my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
print(my_date_time)

type(my_date_time) # datetime.datetime

my_date_time.day
my_date_time.month

first_two = [datetime(2016,1,1), datetime(2016,1,2)]
type(first_two) # list

first_two

dt_ind = pd.DatetimeIndex(first_two)
dt_ind

data = np.random.randn(2,2)
data

cols = ['a', 'b']

df = pd.DataFrame(data, dt_ind, cols)
df

df.index.argmax()
df.index.max()
df.index.argmin()
df.index.min()