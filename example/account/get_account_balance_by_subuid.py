from huobi.client.account import AccountClient
from huobi.constant import *

# get accounts
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)
list_obj = account_client.get_account_balance_by_subuid(sub_uid=g_sub_uid)
LogInfo.output_list(list_obj)

