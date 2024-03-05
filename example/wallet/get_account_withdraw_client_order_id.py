from huobi.client.wallet import WalletClient
from huobi.constant import *

wallet_client = WalletClient(api_key=g_api_key,
                             secret_key=g_secret_key)

result = wallet_client.get_account_withdraw_client_order_id(client_order_id="12345")
result.print_object()
