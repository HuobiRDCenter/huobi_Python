import time

from huobi.client.market import MarketClient
from huobi.constant import *


market_client = MarketClient(url=HUOBI_URL_VN)
depth = market_client.get_pricedepth("btcusdt", 5)
print("---- Top 5 bids ----")
i = 0
for entry in depth.bids:
    i = i + 1
    print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))

print("---- Top 5 asks ----")
i = 0
for entry in depth.asks:
    i = i + 1
    print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))