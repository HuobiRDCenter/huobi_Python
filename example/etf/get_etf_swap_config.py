from huobi.client.etf import EtfClient
from huobi.constant import *


etf_client = EtfClient(url=HUOBI_URL_VN)
etf_config = etf_client.get_etf_swap_config("hb10")
etf_config.print_object()
















