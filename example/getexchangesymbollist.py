from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient()
symbol_list = request_client.get_exchange_symbol_list()

#Symbol.print_object_list(symbol_list)

if len(symbol_list):
    for idx, row in enumerate(symbol_list):
        print("------- number " + str(idx) + " -------")
        row.print_object()
        print()



