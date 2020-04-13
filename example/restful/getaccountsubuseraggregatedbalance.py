from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import *
from huobi.model import Account

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
account_balance_list = request_client.get_current_user_aggregated_balance()
print(account_balance_list)
if account_balance_list and len(account_balance_list):
    for balance in account_balance_list:
        print("\tBalance Currency", balance.currency)
        print("\tType", balance.type)
        print("\tBalance", balance.balance)
        print()


