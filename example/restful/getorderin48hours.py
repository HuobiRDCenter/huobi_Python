from huobi import RequestClient
from huobi.model import *

from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")
"""
This interface queries historical orders within the last 48 hours based on search criteria. 
For historical orders that have been completely canceled (state="canceled"), the query range is only within the last 2 hours.
"""
orders = request_client.get_order_in_recent_48hour(symbol=None, start_time=None, end_time=None, size=None, direct=None)
PrintMix.print_data(orders)















