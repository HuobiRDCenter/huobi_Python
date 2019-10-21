import logging

from huobi.client import *
from huobi.constant import *
from huobi.service.account import GetAccountsSelectService
from huobi.utils import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def callback(order_req_obj: 'OrderListRequest'):
    print("---- order list:  ----")
    order_req_obj.print_object()
    print()

# for test, get account-first
account_id = GetAccountsSelectService({"account_type" : AccountType.SPOT}).get_account_id_by_type(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
PrintBasic.print_basic(account_id, "Account ID")


# subscribe the order list info
if account_id > 0:
    trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
    trade_client.req_order_list(symbol="eosusdt", account_id=account_id, callback=callback, order_states = OrderState.CANCELED, client_req_id = "devin-01-1")


