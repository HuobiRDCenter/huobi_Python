from huobi import RequestClient
from huobi.model import *
from huobi.constant.test import *

from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
orders = request_client.get_historical_orders(symbol="xrpusdt", order_state=OrderState.CANCELED, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None)
PrintMix.print_data(orders)


