from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *




request_client = RequestClient(api_key=g_api_key,
                               secret_key=g_secret_key)


result = request_client.sub_uid_management(g_sub_uid, SubUidState.LOCK)
result.print_object()

print()

result = request_client.sub_uid_management(g_sub_uid, SubUidState.UNLOCK)
result.print_object()

