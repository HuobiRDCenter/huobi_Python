
from huobi.client.trade import TradeClient
from huobi.constant import *


def callback(order_req_obj: 'OrderDetailRequest'):
    print("---- order_detail:  ----")
    order_req_obj.print_object()
    print()

order_id = 52799728139
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
trade_client.req_order_detail(order_id, callback, client_req_id="")



