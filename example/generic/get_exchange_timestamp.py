from huobi.client.generic import GenericClient
from huobi.utils import *


generic_client = GenericClient()
ts = generic_client.get_exchange_timestamp()
LogInfo.output(ts)

