from huobi.client.generic import GenericClient
from huobi.utils import *


generic_client = GenericClient()
list_obj = generic_client.get_exchange_currencies()
LogInfo.output("---- Supported currency ----")
for currency in list_obj:
    LogInfo.output(currency)