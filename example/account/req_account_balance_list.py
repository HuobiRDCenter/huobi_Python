

from huobi.client import *
from huobi.constant import *



def callback(account_balance_req: 'AccountBalanceReq'):
    account_balance_req.print_object()



account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_WEBSOCKET_URI_VN)
account_client.req_account_balance(callback=callback, client_req_id = None)






