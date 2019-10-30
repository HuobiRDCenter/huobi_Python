from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import PrintMix
from huobi.model import QueryDirection

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_withdraw_history(currency=None, from_id=0, size=100, direct=QueryDirection.PREV)
if result and len(result):
    for row in result:
        row.print_object()
        print()


