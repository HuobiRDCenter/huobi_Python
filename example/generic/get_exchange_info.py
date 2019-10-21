from huobi.client import *
from huobi.constant import *

generic_client = GenericClient(url=HUOBI_URL_VN)
list_obj = generic_client.get_exchange_info()
print("---- Supported symbols ----")
for symbol in list_obj.symbol_list:
    print(symbol.symbol)
    #symbol.print_object() # to print details

print("---- Supported currencies ----");
for currency in list_obj.currencies:
    print(currency)
