from huobi.client.subuser import SubuserClient
from huobi.constant import *


subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
deposit_history = subuser_client.get_sub_user_deposit_history(sub_uid=g_sub_uid)
deposit_history.print_object()

