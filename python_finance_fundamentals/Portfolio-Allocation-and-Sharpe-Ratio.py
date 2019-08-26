import numpy as np
import pandas as pd
import quandl

start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01') 

aapl = quandl.get('WIKI/AAPL.11', start_date=start,end_date=end)
cisco = quandl.get('WIKI/CSCO.11', start_date=start,end_date=end)
ibm = quandl.get('WIKI/IBM.11', start_date=start,end_date=end)
amzn = quandl.get('WIKI/AMZN.11', start_date=start,end_date=end)
aapl

# get first adjusted price for apple
aapl.iloc[0]['Adj. Close'] # 52.848786580038

# create a normalized return 
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close'] / stock_df.iloc[0]['Adj. Close']
aapl.head()
aapl.tail()

# 30% in apple
# 20% in cisco
# 40% in amazon
# 10% in ibm
# create allocation column
for stock_df, allo in zip((aapl,cisco,ibm,amzn),[.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo
    
aapl.head()

# create allocation column
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Position Values'] = stock_df['Allocation']*1000000
aapl.head()

all_pos_vals = [aapl['Position Values'], cisco['Position Values'],
                ibm['Position Values'], amzn['Position Values']]

portfolio_val = pd.concat(all_pos_vals,axis=1)
portfolio_val.head()
# add columns names
portfolio_val.columns = ['AAPL Pos', 'CISCO Pos', 'IBM Pos', 'AMZN Pos']

# add Total column 
portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)
portfolio_val.head()

# plot the total portfolio value
import matplotlib.pyplot as plt 
portfolio_val['Total Pos'].plot(figsize=(10,8))
plt.title('Total Portfolio Value')

# plot by individual plot
portfolio_val.drop('Total Pos',axis=1).plot(figsize=(10,8))
plt.title('Individual Stock Performance')