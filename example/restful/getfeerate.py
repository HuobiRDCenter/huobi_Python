from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_fee_rate(symbols="htusdt,btcusdt")
PrintMix.print_data(result)


