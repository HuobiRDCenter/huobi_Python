
from huobi.client.wallet import WalletClient
from huobi.constant import *
from huobi.utils import LogInfo

wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = wallet_client.get_sub_user_deposit_address(sub_uid=g_sub_uid, currency="btc")
LogInfo.output_list(list_obj)



