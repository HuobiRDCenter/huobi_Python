from huobi import RequestClient


request_client = RequestClient()
trade_list = request_client.get_historical_trade("btcusdt", 5)
for trade in trade_list:
    trade.print_object()
    print()
