from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient()
symbol_list = request_client.get_exchange_symbol_list()
PrintMix.print_data(symbol_list)


