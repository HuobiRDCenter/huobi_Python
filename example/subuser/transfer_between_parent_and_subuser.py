from huobi.client.account import AccountClient
from huobi.client.subuser import SubuserClient
from huobi.constant import *

subuser_client = SubuserClient(api_key=g_api_key,
                               secret_key=g_secret_key)

result = subuser_client.transfer_between_parent_and_subuser(sub_uid=178211, currency="178211", amount=178211,
                                                            transfer_type=TransferMasterType.IN, client_order_id="178211")
result.print_object()
