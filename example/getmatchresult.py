from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")

match_list = request_client.get_match_result(symbol="htusdt")
PrintMix.print_data(match_list)


