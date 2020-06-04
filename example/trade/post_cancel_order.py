from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
symbol_test = "eosusdt"


order_id = trade_client.create_order(symbol=symbol_test, account_id=g_account_id, order_type=OrderType.BUY_LIMIT, source=OrderSource.API, amount=18, price=0.292)
LogInfo.output("created order id : {id}".format(id=order_id))
canceled_order_id  = trade_client.cancel_order(symbol_test, order_id)
if canceled_order_id == order_id:
    LogInfo.output("cancel order {id} done".format(id=canceled_order_id))
else:
    LogInfo.output("cancel order {id} fail".format(id=canceled_order_id))
