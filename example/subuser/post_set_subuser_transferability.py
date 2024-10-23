from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
sub_uids = '122946475'

transferability_result = subuser_client.post_set_subuser_transferability(sub_uids, False)
LogInfo.output_list(transferability_result)
