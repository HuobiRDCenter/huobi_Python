from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key,
                               secret_key=g_secret_key)

list_obj = subuser_client.post_user_initiated_credit(user_id=41262769, account_id=31260495, currency="usdt", amount=10,
                                                     transaction_id=17)
LogInfo.output_list(list_obj)
