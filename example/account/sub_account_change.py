import logging
from huobi.client import AccountClient
from huobi.constant import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


def callback(account_change_event: 'AccountChangeEvent'):
    account_change_event.print_object()
    print()


account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              url=HUOBI_WEBSOCKET_URI_VN)
account_client.sub_account_change(BalanceMode.TOTAL, callback)
