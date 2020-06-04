
from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)
transfer_order_id = account_client.transfer_between_parent_and_subuser(sub_uid=g_sub_uid, currency="usdt", amount=10, transfer_type=TransferMasterType.OUT)
LogInfo.output("transfer from master to subuser Order Id : {id}".format(id=transfer_order_id))

transfer_order_id = account_client.transfer_between_parent_and_subuser(sub_uid=g_sub_uid, currency="usdt", amount=10, transfer_type=TransferMasterType.IN)
LogInfo.output("transfer from subuser to master Order Id : {id}".format(id=transfer_order_id))



