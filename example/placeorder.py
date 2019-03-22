from huobi import RequestClient
from huobi.model import *

request_client = RequestClient(api_key="xxxxxx",
                               secret_key="xxxxxx")
order_id = request_client.create_order("btcusdt", AccountType.SPOT, OrderType.BUY_LIMIT, 1.0, 1.0)
request_client.cancel_order("btcusdt", order_id)
