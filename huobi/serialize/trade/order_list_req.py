import gzip

from huobi.constant import AccountType
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model.trade import *


class OrderListReqSerial:

    @staticmethod
    def json_parse(json_data, account_type_map):
        req_obj = OrderListReq()
        error_code = json_data.get_int("err-code")
        req_obj.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        req_obj.client_req_id = json_data.get_string("cid")
        req_obj.topic = json_data.get_string("topic")
        req_obj.symbol = json_data.get_string_or_default("symbol", "")
        if error_code == 0:   # only get data for successful request
            order_list_json = json_data.get_array("data")

            order_list = list()
            for order_json in order_list_json.get_items():
                account_id = order_json.get_int("account-id")
                account_type = AccountType.INVALID
                if account_id in account_type_map:
                    account_type = account_type_map[account_id]
                order_obj = Order.json_parse(order_json, account_type)
                order_list.append(order_obj)
            req_obj.order_list = order_list

        return req_obj

    @staticmethod
    def update_symbol(req_obj: 'OrderListRequest', symbol=None):
        if symbol and len(symbol):
            req_obj.symbol = symbol   # update by setting value
        else:
            if len(req_obj.order_list):
                for order_obj in req_obj.order_list:
                    req_obj.symbol = order_obj.symbol   # update by order symbol
                    break

        return req_obj






