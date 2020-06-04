
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = trade_client.get_feerate(symbols="htusdt,btcusdt,eosusdt")
LogInfo.output_list(list_obj)