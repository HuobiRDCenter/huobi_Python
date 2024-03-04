from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.utils import *
import time

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)
transfer_order_id = account_client.transfer_between_futures_and_pro(currency="trx", amount=200,
                                                                    transfer_type=TransferFuturesPro.TO_FUTURES)
LogInfo.output("transfer from pro to future Order Id : {id}".format(id=transfer_order_id))

# need wait a minute
time.sleep(2)

transfer_order_id = account_client.transfer_between_futures_and_pro(currency="trx", amount=200,
                                                                    transfer_type=TransferFuturesPro.TO_PRO)
LogInfo.output("transfer from future to pro Order Id : {id}".format(id=transfer_order_id))
