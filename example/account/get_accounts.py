from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.service.account.get_accounts_select import GetAccountsSelectService

# get accounts
account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
list_obj = account_client.get_accounts()
if len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()

#get accounts, key is account id
dict_obj = GetAccountsSelectService({}).get_accounts_key_id(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
if len(dict_obj):
    for account_id, obj in dict_obj.items():
        print("========= " + str(account_id) + " =========")
        obj.print_object()
        print()


#get account, key is account type, value is account id list
dict_obj = GetAccountsSelectService({}).get_accounts_key_type(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
if len(dict_obj):
    for account_type, obj_list in dict_obj.items():
        print("========= " + account_type + " =========")
        if obj_list and len(obj_list):
            for obj in obj_list:
                obj.print_object()
                print()


# for type spot
account_type_spot = AccountType.SPOT
accounts = GetAccountsSelectService({"account_type":account_type_spot}).get_accounts_id_by_type(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
if accounts and len(accounts):
    for account_id in accounts:
        print(account_type_spot, ":", str(account_id))
        print()

# for type margin
account_type_margin = AccountType.MARGIN
accounts = GetAccountsSelectService({"account_type":account_type_margin}).get_accounts_id_by_type(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
if accounts and len(accounts):
    for account_id in accounts:
        print(account_type_margin, ":", str(account_id))
