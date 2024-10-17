from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
sub_uid = '122946475'
access_key = '7ab679d7-b9fee8ed-9cd4cd8a-bgbfh5tv3f'

result = subuser_client.post_subuser_apikey_deletion(sub_uid, access_key)
LogInfo.output(result)
