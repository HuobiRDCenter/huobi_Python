from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import *
from huobi.model import Account


# case 1: TRX withdraw and cancel
client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


withdraw_id = client.post_create_withdraw(address="xxxx",
                                                     amount=40, currency="trx", fee=1,
                                                     chain=None, address_tag=None)

print("Create Withdraw ID ", withdraw_id)

withdraw_id_ret = client.post_cancel_withdraw(withdraw_id=withdraw_id)
print("Cancel Withdraw ", withdraw_id_ret)


# case 2: USDT withdraw and cancel
client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id = client.post_create_withdraw(address="0xxxxxxxxx",
                                                     amount=2, currency="usdt", fee=1,
                                                     chain="usdterc20", address_tag=None)

withdraw_id_ret = client.post_cancel_withdraw(withdraw_id=withdraw_id)
print("Cancel Withdraw ", withdraw_id_ret)


# case 3: USDT withdraw and cancel
client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id = client.post_create_withdraw(address="xxxxxx",
                                                     amount=2, currency="usdt", fee=0,
                                                     chain="trc20usdt", address_tag=None)
print("Create Withdraw ID ", withdraw_id)

withdraw_id_ret = client.post_cancel_withdraw(withdraw_id=withdraw_id)
print("Cancel Withdraw ", withdraw_id_ret)




