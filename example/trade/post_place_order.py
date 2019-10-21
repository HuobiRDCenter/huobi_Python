from huobi.client import *
from huobi.constant import *
from huobi.constant.test import *


from huobi.service.account import GetAccountsSelectService

account_id = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_account_id_by_type(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
print(account_id)

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
symbol_test = "eosusdt"


order_id = trade_client.create_order_by_type(symbol=symbol_test, account_type=AccountType.SPOT, order_type=OrderType.BUY_LIMIT, amount=1.0, price=0.2)
print("created order id :", order_id)
canceled_order_id  = trade_client.cancel_order(symbol_test, order_id)
if canceled_order_id == order_id:
    print("cancel order ",  canceled_order_id , " done")
else:
    print("cancel order ", canceled_order_id, " fail")



order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.BUY_LIMIT, amount=1.0, price=0.292)
print("created order id :", order_id)
canceled_order_id  = trade_client.cancel_order(symbol_test, order_id)
if canceled_order_id == order_id:
    print("cancel order ",  canceled_order_id , " done")
else:
    print("cancel order ", canceled_order_id, " fail")
