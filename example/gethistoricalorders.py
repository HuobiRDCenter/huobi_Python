from huobi import RequestClient
from huobi.model import *

from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")
orders = request_client.get_historical_orders(symbol="htusdt", order_state=OrderState.FILLED, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None)
PrintMix.print_data(orders)


