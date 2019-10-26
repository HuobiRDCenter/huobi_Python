import logging
from huobi import SubscriptionClient
from huobi.constant.test import *
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key,
                                secret_key=g_secret_key)


def callback(account_event: 'AccountEvent'):
    print("---- Account Change: " + account_event.change_type + " ----")
    for change in account_event.account_change_list:
        print("Account: " + change.account_type)
        print("Currency: " + change.currency)
        print("Balance: " + str(change.balance))
        print("Balance type: " + str(change.balance_type))
        print()


sub_client.subscribe_account_event(BalanceMode.TOTAL, callback)
#sub_client.subscribe_account_event(BalanceMode.AVAILABLE, callback)
