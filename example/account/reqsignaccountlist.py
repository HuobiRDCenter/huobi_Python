import logging
from huobi import SubscriptionClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix, PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(account_balance: 'AccountBalanceRequest'):
    print("---- account_balance:  ----")
    PrintBasic.print_basic(account_balance.timestamp, "Timestamp")
    PrintBasic.print_basic(account_balance.client_req_id, "Client Req ID")
    PrintBasic.print_basic(account_balance.topic, "Topic")
    print("Account List as below : count " + str(len(account_balance.account_list)))
    if len(account_balance.account_list):
        for account in account_balance.account_list:
            PrintBasic.print_basic(account.id, "\tId")
            PrintBasic.print_basic(account.account_type, "\tAccount Type")
            PrintBasic.print_basic(account.account_state, "\tAccount State")
            print("\tAccount ID : " + str(account.id) + " Balance List as below :")
            if len(account.balances):
                for balance in account.balances:
                    PrintBasic.print_basic(balance.currency, "\t\tCurrency")
                    PrintBasic.print_basic(balance.balance_type, "\t\tBalance type")
                    PrintBasic.print_basic(balance.balance, "\t\tBalance")
                    print()
    print()




sub_client.request_account_balance_event(callback=callback, client_req_id = None, auto_close = True)


