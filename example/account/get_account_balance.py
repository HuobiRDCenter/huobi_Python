from huobi.client import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
account_balance_list = account_client.get_account_balance()
if len(account_balance_list):
    for account_balance_obj in account_balance_list:
        account_balance_obj.print_object()
        print()
