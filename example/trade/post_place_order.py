from huobi.client import TradeClient
from huobi.constant import *
from huobi.constant.test import *


from huobi.service.account import GetAccountsSelectService

accounts = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_accounts_id_by_type(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
account_id = 0
if accounts and len(accounts):
    account_id = accounts[0]
print("=========select first account:", account_id)

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
symbol_test = "eosusdt"
order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.BUY_LIMIT, amount=1.0, price=0.292)
print("created order id :", order_id)

canceled_order_id  = trade_client.cancel_order(symbol_test, order_id)
if canceled_order_id == order_id:
    print("cancel order ",  canceled_order_id , " done")
else:
    print("cancel order ", canceled_order_id, " fail")
