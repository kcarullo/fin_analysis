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


np.random.seed(101)
num_ports = 5000
all_weights = np.zeros((num_ports,len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for ind in range(num_ports):
    
    # weights
    weights = np.array(np.random.random(4))
    weights = weights/np.sum(weights)
    
    # Save weights 
    all_weights[ind,:] = weights 
    
    # expected return 
    ret_arr[ind] = np.sum((log_ret.mean() * weights) * 252) # 252 trading days 
    
    # expected valatility 
    vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252,weights)))
    
    # Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]

sharpe_arr.max()

sharpe_arr.argmax()

all_weights[1420,:]

max_sr_ret = ret_arr[1420]
max_sr_vol = vol_arr[1420]


# visualize the sharpe ratio
plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

plt.scatter(max_sr_vol, max_sr_ret, c='red', s=50, edgecolors='black')


def get_ret_vol_sr(weights):
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252, weights)))
    sr = ret/vol
    return np.array([ret,vol,sr])

from scipy.optimize import minimize

def neg_sharpe(weights):
    return get_ret_vol_sr(weights)[2] * -1

def check_sum(weights):
    # return 0 if the sum of the weights is 1
    return np.sum(weights) - 1

cons = ({'type':'eq','fun':check_sum})

bounds = ((0,1),(0,1),(0,1),(0,1))

initial_guess = [0.25,0.25,0.25,0.25]

optimal_results = minimize(neg_sharpe,initial_guess,method='SLSQP', bounds=bounds,
                           constraints=cons)
optimal_results
optimal_results.x
get_ret_vol_sr(optimal_results.x)

# efficient frontier
frontier_y = np.linspace(0,0.3,100)
def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]

frontier_volatility = []

for possible_return in frontier_y:
    cons = ({'type':'eq', 'fun':check_sum},
            {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[0]-possible_return})
    
    result = minimize(minimize_volatility, initial_guess, method='SLSQP',
                      bounds=bounds, constraints=cons)
    
    frontier_volatility.append(result['fun'])
    
# visualize the sharpe ratio
plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

plt.plot(frontier_volatility, frontier_y, 'g--', linewidth=3)