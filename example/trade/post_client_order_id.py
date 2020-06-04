from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *
import time

symbol_test = "eosusdt"
client_order_id_header = str(int(time.time()))
client_order_id_test = "client_" + client_order_id_header +"_order"  # unique id in 24hours

account_id = g_account_id
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
order_id = trade_client.create_order(symbol=symbol_test,
                                     account_id=account_id,
                                     order_type=OrderType.BUY_LIMIT,
                                     source=OrderSource.API,
                                     amount=20,
                                     price=0.26,
                                     client_order_id=client_order_id_test,
                                     stop_price=0.11,
                                     operator="gte")
LogInfo.output("======= create new order id : {order_id} with client id {client_id} =======".format(order_id=(order_id),
                                                                                 client_id=client_order_id_test))

orderObj = trade_client.get_order(order_id=order_id)
LogInfo.output("======= get order by order id : {order_id} =======".format(order_id=order_id))
orderObj.print_object()

orderObj = trade_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
LogInfo.output("======= get order by client order id : {client_id} =======".format(client_id=client_order_id_test))
orderObj.print_object()

trade_client.cancel_client_order(client_order_id=client_order_id_test)
LogInfo.output("======= cancel order by client order id : {client_id} =======".format(client_id=client_order_id_test))

orderObj = trade_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
LogInfo.output("======= get order by client order id : {client_id} after cancel =======".format(client_id=client_order_id_test))
orderObj.print_object()
