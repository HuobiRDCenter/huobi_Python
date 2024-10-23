from huobi.client.algo import AlgoClient
from huobi.constant import *
from huobi.utils import *

symbol_test = "adausdt"
account_id = g_account_id

algo_client = AlgoClient(api_key=g_api_key, secret_key=g_secret_key)
result = algo_client.get_order_history(symbol_test, AlgoOrderStatus.TRIGGERED)
LogInfo.output_list(result)
