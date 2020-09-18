from huobi.client.subuser import SubuserClient
from huobi.constant import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)

subUid = 122946475
access_key = "abc"
note = "test"
permission = 'readOnly,trade'

result = subuser_client.post_subuser_apikey_modification(subUid, access_key, permission=permission, note=note)
result.print_object()
