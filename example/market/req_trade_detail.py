import logging

from huobi.client import *
from huobi.constant import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)





def callback(trade_req: 'TradeDetailReq'):
    print("---- trade_event:  ----")
    trade_req.print_object()
    print()



market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN)
market_client.req_trade_detail("btcusdt,eosusdt", callback)


