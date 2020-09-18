from huobi.client.algo import AlgoClient
from huobi.constant import *
from huobi.utils import *

symbol_test = "adausdt"
account_id = g_account_id

orders_to_cancel = ["test003", "test001"]
algo_client = AlgoClient(api_key=g_api_key, secret_key=g_secret_key)
result = algo_client.cancel_orders(orders_to_cancel)
result.print_object()

# order_id = algo_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.BUY_MARKET, source=OrderSource.API, amount=5.0, price=1.292)
# LogInfo.output("created order id : {id}".format(id=order_id))
#
# order_id = algo_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.SELL_MARKET, source=OrderSource.API, amount=1.77, price=None)
# LogInfo.output("created order id : {id}".format(id=order_id))
