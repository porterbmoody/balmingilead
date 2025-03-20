#%%



import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import backtrader as bt
import matplotlib.dates as mdates

cerebro = bt.Cerebro()

class SmaCross(bt.Strategy):
    params = (('fast', 10), ('slow', 30),)

    def __init__(self):
        sma_fast = bt.ind.SMA(period=self.p.fast)
        sma_slow = bt.ind.SMA(period=self.p.slow)
        self.crossover = bt.ind.CrossOver(sma_fast, sma_slow)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        else:
            if self.crossover < 0:
                self.sell()

data = yf.download('META', start='2025-03-01', end='2025-03-25').reset_index()
data = pd.DataFrame(data)
fig, ax = plt.subplots()

plt.figure(figsize=(16,8))
plt.plot(data['Date'], data['Close'], label='Close')
plt.plot(data['Date'], data['High'], label='High')
plt.plot(data['Date'], data['Low'], label='Low')
plt.plot(data['Date'], data['Open'], label='Open')
plt.title("Meta")
plt.ylabel("Price (USD)")
plt.xlabel("Date")
plt.legend()
plt.grid(True, linestyle='--')
plt.style.use("dark_background")

ax.set_xticks(data['Date'])
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate(rotation=90)


#%%
# cerebro.adddata(data)

plt.figure(figsize=(16,8))
plt.plot(cerebro.broker.get_value(), label='Portfolio Value')

# plt.plot(data['Close'], label='Close')
plt.legend()
plt.show()

# %%


