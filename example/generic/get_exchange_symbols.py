from huobi.client import *
from huobi.constant import *

generic_client = GenericClient(url=HUOBI_URL_VN)
list_obj = generic_client.get_exchange_symbols()
if len(list_obj):
    for idx, row in enumerate(list_obj):
        print("------- number " + str(idx) + " -------")
        row.print_object()
        print()



