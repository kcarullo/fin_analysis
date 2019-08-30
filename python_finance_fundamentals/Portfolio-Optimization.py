import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('AAPL_CLOSE', index_col='Date',parse_dates=True)
cisco = pd.read_csv('CISCO_CLOSE', index_col='Date',parse_dates=True)
ibm = pd.read_csv('IBM_CLOSE', index_col='Date',parse_dates=True)
amzn = pd.read_csv('AMZN_CLOSE', index_col='Date',parse_dates=True)
aapl.head()

stocks = pd.concat([aapl, cisco, ibm, amzn], axis=1)
stocks.head()

# rename the columns 
stocks.columns = ['aapl', 'cisco', 'ibm', 'amzn']
stocks.head()

# Mean daily return 
stocks.pct_change(1).mean()

# correlation between the returns 
stocks.pct_change(1).corr()

#log returns 
log_ret = np.log(stocks/stocks.shift(1))
log_ret.head()

log_ret.hist(bins=100, figsize=(12,8))
plt.tight_layout()

log_ret.mean()
log_ret.cov() * 252

np.random.seed(101)

print(stocks.columns)

weights = np.array(np.random.random(4))

print("Random Weights")
print(weights)

print("Rebalance")
weights = weights/np.sum(weights)
print(weights)

# expected return 
print('Expected Portfolio Return')
exp_return = np.sum((log_ret.mean() * weights) * 252) # 252 trading days 

# expected valatility 
print('Expected Volatility')
exp_vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252,weights)))

# Sharpe Ratio
print('Sharpe Ratio')
SR = exp_return/exp_vol
print(SR)