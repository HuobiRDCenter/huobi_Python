from huobi.client.account import AccountClient
from huobi.constant import *


# get accounts
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)
# list_obj = account_client.get_accounts()
# if list_obj and len(list_obj):
#     for account_obj in list_obj:
#         list_obj = account_client.get_balance(account_id=account_obj.id)
#         LogInfo.output("===== {account_id} , {account_type} =====".format(account_id=account_obj.id, account_type=account_obj.type))
#         if len(list_obj):
#             for obj in list_obj:
#                 if float(obj.balance) > 0.1:  # only show account with balance
#                     obj.print_object()
#                     print()

LogInfo.output("====== (SDK encapsulated api) not recommend for low performance and frequence limitation ======")
account_balance_list = account_client.get_account_balance()
if account_balance_list and len(account_balance_list):
    for account_balance_obj in account_balance_list:
        if account_balance_obj and len(account_balance_obj.list):
            PrintBasic.print_basic(account_balance_obj.id, "ID")
            PrintBasic.print_basic(account_balance_obj.type, "Account Type")
            PrintBasic.print_basic(account_balance_obj.state, "Account State")
            PrintBasic.print_basic(account_balance_obj.subtype, "Subtype")
            for balance_obj in account_balance_obj.list:
                if float(balance_obj.balance) > 0.1:  # only show account with balance
                    balance_obj.print_object("\t")
                    print()
        print()