
from huobi.client.wallet import WalletClient
from huobi.constant import *
from huobi.utils import *


wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.DEPOSIT, currency=None, from_id=1, size=10, direct=QueryDirection.PREV)
LogInfo.output_list(list_obj)

list_obj = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.WITHDRAW, currency=None, from_id=1, size=10, direct=QueryDirection.NEXT)
LogInfo.output_list(list_obj)



