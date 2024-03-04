from huobi.client.account import AccountClient
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.model.trade import OrderDetailReq
from huobi.utils import *


def callback(order_req_obj: 'OrderDetailReq'):
    print("---- order list:  ----")
    order_req_obj.print_object()
    print()


# for test, get spot account
account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
account_spot = account_client.get_account_by_type_and_symbol(account_type=AccountType.SPOT, symbol=None)

# request the order list info
if account_spot and account_spot.id:
    trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
    PrintBasic.print_basic(account_spot.id, "Account ID")
    trade_client.req_order_list(symbol="eosusdt", account_id=account_spot.id, callback=callback,
                                order_states=OrderState.CANCELED, client_req_id="xxx-01-1")
