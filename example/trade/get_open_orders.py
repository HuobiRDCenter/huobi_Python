from huobi.client import TradeClient
from huobi.constant import *


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
list_obj = trade_client.get_open_orders(symbol="htusdt", account_id=g_spot_account, direct="prev")
print_obj_list(list_obj)


