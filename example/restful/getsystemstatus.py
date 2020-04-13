from huobi import RequestClient
from huobi.constant.test import *


"""
GET https://status.huobigroup.com/api/v2/summary.json
"""
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
system_status = request_client.get_system_status()
print(system_status)
