from huobi.client.subuser import SubuserClient
from huobi.constant import *

subuser_client = SubuserClient(api_key=g_api_key,
                               secret_key=g_secret_key)

result = subuser_client.post_sub_uid_management(sub_uid=178211, action="lock")
result.print_object()
