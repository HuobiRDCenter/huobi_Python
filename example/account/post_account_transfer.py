from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
transfer_result = account_client.post_account_transfer(36979737, 'spot', 3684354, 122946475, 'spot', 11907558, 'usdt', 1)
transfer_result.print_object()
