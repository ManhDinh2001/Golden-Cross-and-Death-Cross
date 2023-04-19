#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('Name_of_File.csv')
df = df[['Date', 'Price']]
df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
df = df.set_index('Date')

# Create 50-day and 200-day moving averages
df['50-day'] = df['Price'].rolling(window=50).mean()
df['200-day'] = df['Price'].rolling(window=200).mean()

# Create signals based on Golden Cross and Death Cross strategy
df['Signal'] = 0.0
df['Signal'] = np.where(df['50-day'] > df['200-day'], 1.0, 0.0)
df['Position'] = df['Signal'].diff()

# Create a DataFrame to store the buy and sell signals
signals = pd.DataFrame(index=df.index)
signals['Price'] = df['Price']
signals['Signal'] = 0.0
signals['Signal'] = np.where(df['Position'] == 1.0, 'Buy', np.where(df['Position'] == -1.0, 'Sell', 'Hold'))

# Plot the stock price and the buy/sell signals
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(signals['Price'], label='Price')

ax.plot(df['50-day'], label='50-day')
ax.plot(df['200-day'], label='200-day')

ax.plot(signals[signals['Signal']=='Buy'].index, 
        signals['Price'][signals['Signal']=='Buy'],
        marker='^', 
        markersize=10, 
        color='green', 
        linewidth=0, 
        label='Buy')

ax.plot(signals[signals['Signal']=='Sell'].index, 
        signals['Price'][signals['Signal']=='Sell'],
        marker='v', 
        markersize=10, 
        color='red', 
        linewidth=0, 
        label='Sell')

ax.legend(loc='upper left')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.show()

