from huobi.client.generic import GenericClient
from huobi.constant import *

generic_client = GenericClient(url=HUOBI_URL_VN)
ts = generic_client.get_exchange_timestamp()
print("Timestamp", ts)

