from huobi.client.generic import GenericClient
from huobi.utils import *


generic_client = GenericClient()
list_obj = generic_client.get_exchange_info()
LogInfo.output("---- Supported symbols ----")
for symbol in list_obj.symbol_list:
    LogInfo.output(symbol.symbol)

LogInfo.output("---- Supported currencies ----");
for currency in list_obj.currencies:
    LogInfo.output(currency)
