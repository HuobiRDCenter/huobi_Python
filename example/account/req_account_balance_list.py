from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.model.account import AccountBalanceReq


def callback(account_balance_req: 'AccountBalanceReq'):
    account_balance_req.print_object()


account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
account_client.req_account_balance(callback=callback, client_req_id=None)
