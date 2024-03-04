from huobi.client.etf import EtfClient
from huobi.constant import *

etf_client = EtfClient(api_key=g_api_key, secret_key=g_secret_key)
etf_client.post_etf_swap_in("hb10", 1000)

















