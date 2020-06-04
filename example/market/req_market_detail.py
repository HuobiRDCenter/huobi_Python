from huobi.client.market import MarketClient
from huobi.model.market import *



def callback(obj_event: 'MarketDetailReq'):
    obj_event.print_object()
    print()


sub_client = MarketClient()
sub_client.req_market_detail("btcusdt", callback)
