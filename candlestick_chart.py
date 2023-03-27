import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from mplfinance.original_flavor import candlestick_ohlc

company = 'MSFT'

# time frame
start = dt.datetime(2022, 1, 1)
end = dt.datetime.now()

# Load data
data = yf.download(company, start, end)

# restructuring data

data = data[['Open', 'High', 'Low', 'Close']]

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdate.date2num)

# Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title(company+' Share price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
plt.show()
