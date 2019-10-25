from huobi.client import *
from huobi.constant import *

market_client = MarketClient(url=HUOBI_URL_VN)
obj = market_client.get_market_detail_merged("btcusdt")
obj.print_object()



