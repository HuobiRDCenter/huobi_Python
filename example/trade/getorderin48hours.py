from huobi import RequestClient
from huobi.model import *

from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")
orders = request_client.get_order_recent_48hour(symbol=None, start_time=None, end_time=None, size=None, direct=None)
PrintMix.print_data(orders)















