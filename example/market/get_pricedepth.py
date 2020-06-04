
from huobi.client.market import MarketClient
from huobi.utils import *


market_client = MarketClient()
symbol = "btcusdt"
depth_size = 6
depth = market_client.get_pricedepth(symbol, DepthStep.STEP0, depth_size)
LogInfo.output("---- Top {size} bids ----".format(size=len(depth.bids)))
i = 0
for entry in depth.bids:
    i = i + 1
    LogInfo.output(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))

LogInfo.output("---- Top {size} asks ----".format(size=len(depth.asks)))

i = 0
for entry in depth.asks:
    i = i + 1
    LogInfo.output(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))