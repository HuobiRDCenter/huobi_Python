from huobi import RequestClient
from huobi.constant.test import *


def print_obj_list(list_obj):
    if list_obj and len(list_obj):
        for obj in list_obj:
            obj.print_object()
            print()

client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = client.get_account_deposit_address(currency="usdt")
print_obj_list(list_obj)
