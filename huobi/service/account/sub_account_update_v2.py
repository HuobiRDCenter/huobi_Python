from huobi.utils import *

from huobi.connection.subscribe_client import SubscribeClient
from huobi.model.account import *


class SubAccountUpdateV2Service:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        mode = self.params["mode"]

        def subscription(connection):
            connection.send(accounts_update_channel(mode))

        def parse(dict_data):
            account_change_event = AccountUpdateEvent()
            account_change_event.ch = dict_data.get("ch")
            data = dict_data.get("data", {})
            if data and len(data):
                account_change_event.data = default_parse_list_dict(data, AccountUpdate)

            return account_change_event

        SubscribeClient(**kwargs).execute_subscribe_v2(subscription,
                                                       parse,
                                                       callback,
                                                       error_handler,
                                                       is_trade=True)
