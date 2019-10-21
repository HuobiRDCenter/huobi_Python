import logging
from huobi.client import *
from huobi.constant import *


logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)



def callback(upd_event: 'OrderUpdateEvent'):
    print("---- order update : ----")
    upd_event.print_object()
    print()


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
trade_client.sub_order_update("eosusdt", callback)
