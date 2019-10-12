from huobi.client.market import MarketClient
from huobi.constant.definition import CandlestickInterval



market_client = MarketClient()
candlestick_list = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN1, 10)
print("---- 1 min candlestick for btcusdt ----")
for item in candlestick_list:
    item.print_object()
    print()
















