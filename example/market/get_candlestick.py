from huobi.client.market import MarketClient
from huobi.constant import *


market_client = MarketClient(url=HUOBI_URL_VN)
list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN1, 10)
print("---- 1 min candlestick for btcusdt ----")
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()
















