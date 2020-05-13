from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import *
from huobi.model import Account
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
account_balance_list = request_client.get_account_balance()
if account_balance_list and len(account_balance_list):
    for account in account_balance_list:
        print("======= ID", account.id, "=======")
        print("Account Status", account.account_state)
        print("Account Type", account.account_type)
        print("Subtype", account.subtype)
        if  account.balances and len(account.balances):
            for balance in account.balances:
                print("\tBalance Currency", balance.currency)
                print("\tBalance Type", balance.balance_type)
                print("\tBalance", balance.balance)
                print()
        print()

