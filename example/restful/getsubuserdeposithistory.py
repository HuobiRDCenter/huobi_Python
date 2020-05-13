from huobi import RequestClient
from huobi.constant.test import *


def print(deposit_history):
    if deposit_history.data and len(deposit_history.data):
        print(deposit_history.nextId)
        for obj in deposit_history.data:
            obj.print_object()
            print()

client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
deposit_history = client.get_sub_user_deposit_history(sub_uid=g_sub_uid)
print(deposit_history)