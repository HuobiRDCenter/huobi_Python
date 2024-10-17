import time


from huobi.connection.websocket_req_client import *
from huobi.model.trade import *
from huobi.utils import *


class ReqOrderListService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]
        account_id = self.params["account-id"]
        order_states = self.params["states"]
        client_req_id = self.params["client-req-id"]

        def subscription(connection):
            connection.send(request_order_list_channel(symbol=symbol, account_id=account_id, states_str=order_states, client_req_id=client_req_id, more_key=self.params))

        def parse(dict_data):
            order_update_event = default_parse(dict_data, OrderListReq, OrderListItem)

            return order_update_event

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)







