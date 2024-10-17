from huobi.client.algo import AlgoClient
from huobi.constant import *

account_id = g_account_id
client_order_id = "test002"

# get specific order by clientOrderId
algo_client = AlgoClient(api_key=g_api_key, secret_key=g_secret_key)
result = algo_client.get_order(client_order_id)
result.print_object()
