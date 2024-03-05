from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

result = account_client.get_account_valuation(account_type="spot", valuation_currency="BTC")
result.print_object()
