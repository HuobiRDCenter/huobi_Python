from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.constant.test import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
symbol_test = "eosusdt"

i = 0
n = 3
order_id_list = []
while(i<n):
    order_id = trade_client.create_order(symbol=symbol_test, account_id=g_account_id, order_type=OrderType.BUY_LIMIT, amount=1.0, price=0.292)
    print("created order id :", order_id)
    order_id_list.append(order_id)
    i = i+1

result = trade_client.cancel_orders(symbol_test, order_id_list)
result.print_object()


