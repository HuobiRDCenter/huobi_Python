
from huobi.client.trade import TradeClient
from huobi.constant import *


def callback(order_req_obj: 'OrderDetailReq'):
    order_req_obj.print_object()

order_id = 25943298391691
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
trade_client.req_order_detail(order_id, callback, client_req_id="abcde")



