

from huobi.connection.websocket_req_client import *
from huobi.model.trade import *
from huobi.utils import *


class ReqOrderDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        order_id = self.params["order-id"]
        client_req_id = self.params["cid"]

        def subscription(connection):
            connection.send(request_order_detail_channel(order_id, client_req_id))

        def parse(dict_data):
            order_update_event = default_parse(dict_data, OrderDetailReq, OrderListItem)

            return order_update_event

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)







