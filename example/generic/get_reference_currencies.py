from huobi.client.generic import GenericClient
from huobi.utils import *


generic_client = GenericClient()

list_obj = generic_client.get_reference_currencies()
LogInfo.output_list(list_obj)


list_obj = generic_client.get_reference_currencies(currency="usdt")
LogInfo.output_list(list_obj)

