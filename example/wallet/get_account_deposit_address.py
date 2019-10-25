
from huobi.client.wallet import WalletClient
from huobi.constant import *


def print_obj_list(list_obj):
    if list_obj and len(list_obj):
        for obj in list_obj:
            obj.print_object()
            print()

wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = wallet_client.get_account_deposit_address(currency="usdt")
print_obj_list(list_obj)





