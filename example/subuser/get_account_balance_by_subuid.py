from huobi.client.subuser import SubuserClient
from huobi.constant import *

# get accounts
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key,
                              secret_key=g_secret_key)
list_obj = subuser_client.get_account_balance_by_subuid(sub_uid=g_sub_uid)
LogInfo.output_list(list_obj)

