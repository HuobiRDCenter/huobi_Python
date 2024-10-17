from huobi.client.algo import AlgoClient
from huobi.constant import *

algo_client = AlgoClient(api_key=g_api_key,
                            secret_key=g_secret_key)

result = algo_client.post_cancel_all_after(timeout=10)
result.print_object()
