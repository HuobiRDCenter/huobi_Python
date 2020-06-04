from huobi.client.etf import EtfClient


etf_client = EtfClient()
etf_config = etf_client.get_etf_swap_config("hb10")
etf_config.print_object()










