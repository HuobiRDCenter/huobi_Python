import logging
from huobi.client import TradeClient
from huobi.constant import *



logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)



def callback(order_req_obj: 'OrderDetailRequest'):
    print("---- order_detail:  ----")
    order_req_obj.print_object()
    print()


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
trade_client.req_order_detail(order_id, callback, client_req_id="")



