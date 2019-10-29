from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.model.market import *


def callback(obj_event: 'MarketDetailEvent'):
    obj_event.print_object()
    print()


market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN)
market_client.sub_market_detail("btcusdt", callback)