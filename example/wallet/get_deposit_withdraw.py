
from huobi.client import WalletClient
from huobi.constant import *


def print_obj_list(list_obj):
    if list_obj and len(list_obj):
        for obj in list_obj:
            obj.print_object()
            print()

wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
#list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.DEPOSIT, currency="eos", from_id=1, size=10, direct=QueryDirection.PREV)
list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.DEPOSIT, currency=None, from_id=1, size=10, direct=QueryDirection.PREV)
print_obj_list(list_obj)

#list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.WITHDRAW, currency="eos", from_id=1, size=10, direct=QueryDirection.PREV)
list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.WITHDRAW, currency=None, from_id=1, size=10, direct=QueryDirection.PREV)
print_obj_list(list_obj)



