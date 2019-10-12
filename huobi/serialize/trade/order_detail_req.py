
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import *


class OrderDetailReqSerial:


    @staticmethod
    def json_parse(json_data, account_type):
        req_obj = OrderDetailRequest()
        req_obj.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        req_obj.client_req_id = json_data.get_string("cid")
        req_obj.topic = json_data.get_string("topic")
        order_json = json_data.get_object("data")
        account_type = account_type if account_type else AccountType.INVALID
        order_obj = Order.json_parse(order_json, account_type)
        req_obj.symbol = order_obj.symbol
        req_obj.data = order_obj

        return req_obj



