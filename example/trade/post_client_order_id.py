from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.constant.test import *
from huobi.service.account.get_accounts_select import GetAccountsSelectService


symbol_test = "eosusdt"
client_order_id_test = "xxxx"  # unique id in 24hours


accounts = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_accounts_id_by_type(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
account_id = 0
if accounts and len(accounts):
    account_id = accounts[0]
print("=========select first account:", account_id)

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)

order_id = trade_client.create_order(symbol=symbol_test,
                                       account_id=account_id,
                                       order_type=OrderType.BUY_LIMIT,
                                       amount=1.0,
                                       price=0.21,
                                       client_order_id=client_order_id_test,
                                       stop_price=0.11,
                                       operator="gte")
print ("create new order id : ", (str(order_id)), " with client id " + client_order_id_test)
print("\n\n")


orderObj = trade_client.get_order(order_id=order_id)
print ("get order by order id : " + (str(order_id)))
orderObj.print_object()
print("\n\n")



orderObj = trade_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
print ("get order by client order id : " + client_order_id_test)
orderObj.print_object()
print("\n\n")


trade_client.cancel_client_order(client_order_id=client_order_id_test)
print ("cancel order by client order id : " + client_order_id_test)
print("\n\n")

orderObj = trade_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
print ("get order by client order id : " + client_order_id_test + " after cancel")
orderObj.print_object()



