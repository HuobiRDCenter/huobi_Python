from huobi.client.etf import EtfClient
from huobi.constant import *
from huobi.utils import *


etf_client = EtfClient(api_key=g_api_key, secret_key=g_secret_key)
etf_list = etf_client.get_etf_swap_list(etf_name="hb10", offset=0, size=20)
LogInfo.output_list(etf_list)
















