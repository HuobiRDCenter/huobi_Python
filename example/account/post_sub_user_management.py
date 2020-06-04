
from huobi.client.account import AccountClient
from huobi.constant import *

# get accounts
account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key)

ret = account_client.post_sub_uid_management(sub_uid=g_sub_uid, action=SubUidAction.LOCK)
ret.print_object()

ret = account_client.post_sub_uid_management(sub_uid=g_sub_uid, action=SubUidAction.UNLOCK)
ret.print_object()