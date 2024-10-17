from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

account_point_result = account_client.get_account_point()
account_point_result.print_object()
