from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

result = account_client.get_account_transfer(from_="spot", to="linear-swap", currency="usdt", amount=100,
                                             margin_account="USDT")
result.print_object()
