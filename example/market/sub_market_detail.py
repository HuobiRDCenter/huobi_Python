from huobi.client.market import MarketClient
from huobi.model.market import *


def callback(obj_event: 'MarketDetailEvent'):
    obj_event.print_object()
    print()


market_client = MarketClient()
market_client.sub_market_detail("btcusdt", callback)