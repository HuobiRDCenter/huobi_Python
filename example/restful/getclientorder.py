from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix
import time

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

client_order_id_tmp = "abc022505"



symbol_test = "eosusdt"

print("\n============== get order by client id ===============\n")
order_obj = request_client.get_order_by_client_order_id(client_order_id=client_order_id_tmp)
order_obj.print_object()



