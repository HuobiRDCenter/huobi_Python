import logging
from huobi.client import AccountClient
from huobi.constant import *
from huobi.service.account import *


logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
list_obj = account_client.get_accounts()
if len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()


dict_obj = GetAccountsSelectService({}).request_by_id(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_URL_VN)
if len(dict_obj):
    for account_id, obj in dict_obj.items():
        print("========= " + str(account_id) + " =========")
        obj.print_object()
        print()
