
from huobi.client.wallet import WalletClient
from huobi.constant import *
from huobi.utils import *


wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = wallet_client.get_account_withdraw_address(currency="usdt")
LogInfo.output_list(list_obj)
