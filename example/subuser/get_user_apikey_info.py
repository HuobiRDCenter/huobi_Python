from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
apikey_info = subuser_client.get_user_apikey_info("122946475")
LogInfo.output_list(apikey_info)
