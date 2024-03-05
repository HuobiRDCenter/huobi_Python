from huobi.client.subuser import SubuserClient
from huobi.constant import *

subuser_client = SubuserClient(api_key=g_api_key,
                               secret_key=g_secret_key)

result = subuser_client.get_subuser_account_list(sub_uid=12345)
result.print_object()
