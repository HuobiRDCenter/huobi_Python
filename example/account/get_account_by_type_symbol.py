from huobi.client.account import AccountClient
from huobi.client.margin import MarginClient
from huobi.constant import *

# get accounts
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)

LogInfo.output("========= case 1 get spot (SDK encapsulated api) =========")
account_obj = account_client.get_account_by_type_and_symbol(account_type=AccountType.SPOT, symbol=None)
account_obj.print_object()

LogInfo.output("========= case 2 get margin-eosusdt (SDK encapsulated api) =========")
account_obj = account_client.get_account_by_type_and_symbol(account_type=AccountType.MARGIN, symbol="eosusdt")
if account_obj:
    account_obj.print_object()

LogInfo.output("========= case 3 get margin-eosusdt (SDK encapsulated api) =========")
account_obj = account_client.get_account_by_type_and_symbol(account_type=AccountType.SUPER_MARGIN, symbol=None)
if account_obj:
    account_obj.print_object()

LogInfo.output("========= case 4 get margin-eosusdt (original api, supported) =========")
margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = margin_client.get_margin_account_balance(symbol="eosusdt")
LogInfo.output_list(list_obj)

LogInfo.output("========= case 5 get cross-margin (original api, supported) =========")
account_balance = margin_client.get_cross_margin_account_balance()
account_balance.print_object()