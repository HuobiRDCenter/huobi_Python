from huobi import RequestClient
from huobi.constant.test import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
account_history_list = request_client.get_account_history(account_id=g_account_id)
if account_history_list and len(account_history_list):
    for account_history in account_history_list:
        account_history.print_object()
        print()


