from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *

client_order_id_test = "xxxxxx"  # unique id in 24hours

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
orderObj = trade_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
LogInfo.output("======= get order by client order id : {client_id} =======".format(client_id=client_order_id_test))
orderObj.print_object()


