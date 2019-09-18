from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")
result = request_client.get_fee_rate(symbols="htusdt,btcusdt")
PrintMix.print_data(result)


