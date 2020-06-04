
from huobi.utils import *

from huobi.connection.websocket_req_client import *
from huobi.model.account import *



class ReqAccountBalanceService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        client_req_id = self.params["client_req_id"]
        def subscription(connection):
            connection.send(request_account_list_channel(client_req_id))

        def parse(dict_data):
            req_obj = AccountBalanceReq()
            req_obj.ts = dict_data.get("ts", 0)
            req_obj.topic = dict_data.get("topic", 0)
            req_obj.cid = dict_data.get("cid", 0)
            data_list = dict_data.get("data", [])
            req_obj.data = AccountBalance.json_parse_list(data_list)
            return req_obj

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)



