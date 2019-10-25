from huobi.client.account import AccountClient
from huobi.constant import *

# get accounts
account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
list_obj = account_client.get_account_balance_by_subuid(sub_uid=g_sub_uid)
if len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()

