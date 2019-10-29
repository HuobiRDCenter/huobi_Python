from huobi.client.etf import EtfClient
from huobi.constant import *


etf_client = EtfClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
etf_list = etf_client.get_etf_swap_list(etf_name="hb10", offset=0, size=20)
if etf_list and len(etf_list):
    for etf_list_item in etf_list:
        etf_list_item.print_object()
        print()
















