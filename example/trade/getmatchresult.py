from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

match_list = request_client.get_match_result(symbol="eosusdt")
PrintMix.print_data(match_list)


