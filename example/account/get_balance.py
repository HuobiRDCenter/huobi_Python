from huobi.client.account import AccountClient
from huobi.constant import *

# get accounts
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)
list_obj = account_client.get_balance(account_id=g_account_id)
LogInfo.output_list(list_obj)
