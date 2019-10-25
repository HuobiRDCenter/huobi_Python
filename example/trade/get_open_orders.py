import time

from huobi.client import TradeClient
from huobi.constant import *
from huobi.service.account import GetAccountsSelectService


def print_obj_list(list_obj):
    if list_obj and len(list_obj):
        for obj in list_obj:
            obj.print_object()
            print()

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)

print("\n==============test case 1===============\n")
list_obj = trade_client.get_open_orders_by_type(symbol="htusdt", account_type=AccountType.SPOT, direct="next")
print_obj_list(list_obj)

print("\n==============test case 2===============\n")
accounts = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_accounts_id_by_type(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
if accounts and len(accounts):
    for account_id in accounts:
        list_obj = trade_client.get_open_orders(symbol="htusdt", account_id=account_id, direct="prev")
        print_obj_list(list_obj)


