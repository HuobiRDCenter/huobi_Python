from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintList

request_client = RequestClient()
currencies = request_client.get_exchange_currencies()
PrintList.print_list_data(currencies)
