from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.constant.test import *

client_order_id_test = "xxxxxx"
symbol_test = "eosusdt"

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)



order_id = trade_client.create_order(symbol=symbol_test, account_id=g_account_id,
                                     order_type=OrderType.BUY_LIMIT, amount=1.0,
                                     price=0.292, client_order_id=client_order_id_test)
print("created order id :", order_id, client_order_id_test)
result = trade_client.cancel_client_order(client_order_id=client_order_id_test)
print("cancel result ",  result)

