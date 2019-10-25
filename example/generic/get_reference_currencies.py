from huobi.client import *
from huobi.constant import *

generic_client = GenericClient(url=HUOBI_URL_VN)

list_obj = generic_client.get_reference_currencies()
if len(list_obj):
    for reference_currency in list_obj:
        reference_currency.print_object()


list_obj = generic_client.get_reference_currencies(currency="usdt")
if len(list_obj):
    for reference_currency in list_obj:
        reference_currency.print_object()
