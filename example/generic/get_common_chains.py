from huobi.client.generic import GenericClient
from huobi.constant import *
from huobi.utils import *

generic_client = GenericClient(api_key=g_api_key,
                               secret_key=g_secret_key)

list_obj = generic_client.get_common_chains()
LogInfo.output_list(list_obj)
