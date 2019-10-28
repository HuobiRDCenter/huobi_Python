from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

print("\n==============test case 1===============\n")
result = request_client.get_open_orders(symbol="btcusdt", account_type=AccountType.SPOT, direct="next")
PrintMix.print_data(result)


print("\n==============test case 2===============\n")
result = request_client.get_open_orders(symbol="xrpusdt", account_type=AccountType.MARGIN, direct="prev")
PrintMix.print_data(result)

print("\n==============test case 3===============\n")
result = request_client.get_open_orders(symbol="xrpusdt", account_type=AccountType.SUPER_MARGIN, direct="prev")
PrintMix.print_data(result)

