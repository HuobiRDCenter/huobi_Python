from huobi.client.account import AccountClient
from huobi.constant import *

# get accounts
from huobi.utils import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

account_history = account_client.get_account_history(account_id=g_account_id, start_time=1600827872000, size=4)
LogInfo.output_list(account_history["data"])
LogInfo.output('Next Id: %s' % (account_history["next_id"]))
