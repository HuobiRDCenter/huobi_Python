
from huobi.client.wallet import WalletClient
from huobi.constant import *


wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
deposit_history = wallet_client.get_sub_user_deposit_history(sub_uid=g_sub_uid)
deposit_history.print_object()




