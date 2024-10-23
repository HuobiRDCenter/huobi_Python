from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *
import string
import random

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
userName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
params = {"userList": [
    {
        "userName": userName,
        "note": "huobi"
    }
]}

userList = subuser_client.post_create_subuser(params)
LogInfo.output_list(userList)
