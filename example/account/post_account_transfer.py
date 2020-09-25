from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
# transfer_result = account_client.post_account_transfer(111859319, 'spot', 10354000, 147509118, 'spot', 13956126, 'trx', 3600)
# transfer_result.print_object()

# transfer_result = account_client.post_account_transfer(111859319, 'spot', 10354000, 147991959, 'spot', 14026125, 'usdt', 3600)
# transfer_result.print_object()

transfer_result = account_client.post_account_transfer(111859319, 'spot', 10354000, 141403659, 'spot', 13082796, 'usdt', 32.21)
transfer_result.print_object()
