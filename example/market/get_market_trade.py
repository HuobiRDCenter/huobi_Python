from huobi.client.market import MarketClient
from huobi.constant import HUOBI_URL_VN

market_client = MarketClient(url=HUOBI_URL_VN)
list_obj = market_client.get_market_trade(symbol="eosusdt")
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()













