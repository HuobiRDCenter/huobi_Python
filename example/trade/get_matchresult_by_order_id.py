from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *

order_id_test = 87939085540

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = trade_client.get_match_results_by_order_id(order_id=order_id_test)
LogInfo.output_list(list_obj)
