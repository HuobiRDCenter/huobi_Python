from huobi.client.market import MarketClient
from huobi.constant import HUOBI_URL_VN

market_client = MarketClient(url=HUOBI_URL_VN)
list_obj = market_client.get_history_trade("btcusdt", 6)
if list_obj and len(list_obj):
    for idx, obj in enumerate(list_obj):
        obj.print_object()
        print()
