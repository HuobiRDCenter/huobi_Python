from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key,
                               secret_key=g_secret_key)

list_obj = subuser_client.post_subuser_deduct_mode(sub_uids="178211", deduct_mode="master")
LogInfo.output_list(list_obj)
