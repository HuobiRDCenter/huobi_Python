from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")

print("\n==============test case 1===============\n")
result = request_client.get_open_orders(symbol="htusdt", account_type=AccountType.SPOT, direct="next")
PrintMix.print_data(result)

print("\n==============test case 2===============\n")
result = request_client.get_open_orders(symbol="htusdt", account_type=AccountType.MARGIN, direct="prev")
PrintMix.print_data(result)


