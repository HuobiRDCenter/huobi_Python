from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import LogInfo

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = subuser_client.get_sub_user_deposit_address(sub_uid=g_sub_uid, currency="btc")
LogInfo.output_list(list_obj)



