from huobi.client.market import MarketClient

market_client = MarketClient()
obj = market_client.get_market_detail("btcusdt")
obj.print_object()



