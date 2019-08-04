import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('walmart_stock.csv', index_col = 'Date', parse_dates = True)

df['Open'].plot(figsize=(16,6), title = 'WalMart Stock')

# MOving average first 6 rows are NaN because we input

df.rolling(7).mean().head(14)

df['Open'].plot()
df.rolling(window = 30).mean()['Close'].plot(figsize = (16,6))

# add legend
df['Close 30 Day MA'] = df['Close'].rolling(window = 30).mean()
df[['Close 30 Day MA', 'Close']].plot(figsize = (16, 6))

df['Close'].expanding().mean().plot(figsize=(16,6))


# Close 20 MA
df['Close: 20 Day Mean'] = df['Close'].rolling(20).mean()

# Upper = 20MA + 2*std(20)
df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(20).std())

# Lower = 20MA - 2*std(20)
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(20).std())

# Close

df[['Close', 'Close: 20 Day Mean', 'Upper', 'Lower']].plot(figsize = (16, 6))