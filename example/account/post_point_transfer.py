from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

point_transfer_result = account_client.post_point_transfer(from_uid="111859319", to_uid="124409916", group_id="0",
                                                           amount="10")
point_transfer_result.print_object()
