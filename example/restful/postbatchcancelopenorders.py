from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key,
                               secret_key=g_secret_key)


symbol_test = "eosusdt"
cancel_result = request_client.cancel_open_orders(symbol="btcusdt", account_type=AccountType.SPOT)
PrintMix.print_data(cancel_result)


cancel_result = request_client.cancel_open_orders(symbol="xrpusdt", account_type=AccountType.MARGIN)
PrintMix.print_data(cancel_result)


cancel_result = request_client.cancel_open_orders(symbol="xrpusdt", account_type=AccountType.SUPER_MARGIN)
PrintMix.print_data(cancel_result)


