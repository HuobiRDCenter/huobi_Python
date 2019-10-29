from huobi.client.market import MarketClient
from huobi.constant import *

market_client = MarketClient(url=HUOBI_URL_VN)
obj = market_client.get_market_detail("btcusdt")
obj.print_object()



