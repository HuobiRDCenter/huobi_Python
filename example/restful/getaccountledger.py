from huobi import RequestClient
from huobi.constant.test import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
"""
Note that it is AccountID, not Huobi UID
"""
account_ledger_list = request_client.get_account_ledger(account_id=g_account_id)
if account_ledger_list and len(account_ledger_list):
    for account_ledger in account_ledger_list:
        account_ledger.print_object()
        print()
