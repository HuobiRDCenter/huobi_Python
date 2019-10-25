from huobi.client import AccountClient
from huobi.constant import *
from huobi.service.account import *

# get accounts
account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
list_obj = account_client.get_accounts()
if list_obj and len(list_obj):
    for account_obj in list_obj:
        list_obj = account_client.get_balance(account_id=account_obj.id)
        if len(list_obj):
            for obj in list_obj:
                obj.print_object()
                print()