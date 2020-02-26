import os
if(os.path.exists("huobi/privateconfig.py")):
    from huobi.privateconfig import *
    g_api_key = p_api_key
    g_secret_key = p_secret_key
else:
    g_api_key="yyyyyy"
    g_secret_key="xxxxxx"

g_account_id = 12345678

g_sub_uid = 87654321

