from huobi.client import MarketClient
from huobi.constant import HUOBI_WEBSOCKET_URI_VN
from huobi.model.market import *



def callback(obj_event: 'MarketDetailReq'):
    obj_event.print_object()
    print()


sub_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN, auto_close=True)
sub_client.req_market_detail("btcusdt", callback)
