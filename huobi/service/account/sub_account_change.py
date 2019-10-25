
from huobi.utils import *

from huobi.connection import SubscribeClient
from huobi.model.account import *



class SubAccountChangeService:
    def __init__(self, params):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        model = self.params["model"]

        def subscription(connection):
            connection.send(account_change_channel(model))

        def parse(dict_data):
            account_change_event = AccountChangeEvent()
            account_change_event.op = dict_data.get("op")
            account_change_event.ts = dict_data.get("ts")
            account_change_event.topic = dict_data.get("topic")
            data = dict_data.get("data", {})
            if len(data):
                account_change_event.event = data.get("event")
                account_change_event.account_change_list = default_parse_list_dict(data.get("list", []), AccountChange)

            return account_change_event

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)



