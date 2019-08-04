import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('walmart_stock.csv', index_col = 'Date', parse_dates = True)

df.head()
#reason it skips from 2012-01-06 to 2012-01-09 is 07 and 08 were Sat and Sun

df.tail() 

df.shift(periods=1).head()
# notice 2012-01-03 has NaN where the first df.head() open was 59.970001
# periods shifted the first row down one leaving the NaNs

