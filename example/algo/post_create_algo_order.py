from huobi.client.algo import AlgoClient
from huobi.constant import *
from huobi.utils import *

symbol_test = "adausdt"
account_id = g_account_id

algo_client = AlgoClient(api_key=g_api_key, secret_key=g_secret_key)
order_id = algo_client.create_order(symbol=symbol_test, account_id=account_id, order_side=OrderSide.BUY,
                                    order_type=AlgoOrderType.LIMIT, order_size=65, order_price=0.08, stop_price=0.085,
                                    client_order_id="test004")
LogInfo.output("created order id : {id}".format(id=order_id))
