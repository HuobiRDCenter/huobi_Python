from huobi.client.market import MarketClient
from huobi.utils import *

market_client = MarketClient(init_log=True)
list_obj = market_client.get_market_tickers()
LogInfo.output_list(list_obj)
















