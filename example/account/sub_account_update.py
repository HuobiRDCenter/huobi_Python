from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.model.account.updated import Updated


def callback(account_change_event: 'Updated'):
    account_change_event.print_object()
    print()


account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key,
                               init_log=True)
# account_client.sub_account_update(AccountBalanceMode.TOTAL, callback)
account_client.sub_account_update(AccountBalanceMode.BALANCE, callback)
