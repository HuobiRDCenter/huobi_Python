from huobi.client.account import AccountClient
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


symbol = "eosusdt"

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)

account_spot = account_client.get_account_by_type_and_symbol(account_type=AccountType.SPOT, symbol=None)
account_id_test = account_spot.id

direct_tmp = QueryDirection.NEXT
LogInfo.output("==============test case 1 for {direct}===============".format(direct=direct_tmp))
list_obj = trade_client.get_open_orders(symbol=symbol, account_id=account_id_test, direct=direct_tmp)
LogInfo.output_list(list_obj)

direct_tmp = QueryDirection.PREV
LogInfo.output("==============test case 2 for {direct}===============".format(direct=direct_tmp))
list_obj = trade_client.get_open_orders(symbol=symbol, account_id=account_id_test, direct=direct_tmp)
LogInfo.output_list(list_obj)
