

from huobi.client import *
from huobi.constant import *
from huobi.service.account import GetAccountsSelectService
from huobi.utils import *


def callback(order_req_obj: 'OrderListRequest'):
    print("---- order list:  ----")
    order_req_obj.print_object()
    print()

# for test, get account-first
accounts = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_accounts_id_by_type(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)

# subscribe the order list info
if accounts and len(accounts):
    trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
    for account_id in accounts:
        PrintBasic.print_basic(account_id, "Account ID")
        trade_client.req_order_list(symbol="eosusdt", account_id=account_id, callback=callback, order_states = OrderState.CANCELED, client_req_id = "devin-01-1")


