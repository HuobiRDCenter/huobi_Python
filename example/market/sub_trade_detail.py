import logging

from huobi.client import *
from huobi.constant import *


logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)



def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()

market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN)
market_client.sub_trade_detail("btcusdt,eosusdt", callback)

