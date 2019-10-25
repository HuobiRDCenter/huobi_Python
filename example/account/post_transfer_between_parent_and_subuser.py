import logging
from huobi.client import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
transfer_order_id = account_client.transfer_between_parent_and_subuser(sub_uid=g_sub_uid, currency="usdt", amount=10, transfer_type=TransferMasterType.OUT)
print("transfer Order Id : ", transfer_order_id)


