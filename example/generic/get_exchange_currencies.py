from huobi.client import *
from huobi.constant import *

generic_client = GenericClient(url=HUOBI_URL_VN)
list_obj = generic_client.get_exchange_currencies()
if len(list_obj):
    for currency in list_obj:
        print(currency)
