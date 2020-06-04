from huobi.client.wallet import WalletClient
from huobi.constant import *
from huobi.utils import *


# case 1: TRX withdraw and cancel
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id = wallet_client.post_create_withdraw(address="xxxxxx",
                                                     amount=40, currency="trx", fee=1,
                                                     chain=None, address_tag=None)
LogInfo.output("Create Withdraw ID {id}".format(id=withdraw_id))

withdraw_id_ret = wallet_client.post_cancel_withdraw(withdraw_id=withdraw_id)
LogInfo.output("Cancel Withdraw Id {id} {response_id}".format(id=withdraw_id, response_id=withdraw_id_ret))


# case 2: USDT withdraw and cancel
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id = wallet_client.post_create_withdraw(address="xxxxxx",
                                                     amount=2, currency="usdt", fee=0,
                                                     chain="trc20usdt", address_tag=None)

withdraw_id_ret = wallet_client.post_cancel_withdraw(withdraw_id=withdraw_id)
LogInfo.output("Cancel Withdraw {withdraw_id}, {response_id}".format(withdraw_id=withdraw_id, response_id=withdraw_id_ret))





