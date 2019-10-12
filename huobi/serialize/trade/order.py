from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.constant import *


class OrderSerial:


    # for restful api
    @staticmethod
    def json_parse(json_data, account_type):
        order = Order()
        order.order_id = json_data.get_int("id")
        order.symbol = json_data.get_string("symbol")
        order.price = json_data.get_float("price")
        order.amount = json_data.get_float("amount")
        order.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        order.canceled_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("canceled-at"))
        order.finished_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("finished-at"))
        order.order_type = json_data.get_string("type")
        order.filled_amount = json_data.get_float_or_default("field-amount", json_data.get_float_or_default("filled-amount", 0))
        order.filled_cash_amount = json_data.get_float_or_default("field-cash-amount", json_data.get_float_or_default("filled-cash-amount", 0))
        order.filled_fees = json_data.get_float_or_default("field-fees", json_data.get_float_or_default("filled-fees", 0))
        order.account_type = account_type
        order.source = json_data.get_string("source")
        order.state = json_data.get_string("state")
        order.stop_price = json_data.get_float_or_default("stop-price", 0.0)
        order.operator = json_data.get_string_or_default("operator", "")
        order.next_time = json_data.get_string_or_default("next-time", "")
        return order

    # for order update subscribe
    @staticmethod
    def json_parse_order_update(json_data, account_type):
        order = Order()
        order.order_id = json_data.get_int("id")
        order.symbol = json_data.get_string("symbol")
        order.price = json_data.get_float("price")
        order.amount = json_data.get_float("amount")
        order.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        order.canceled_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("canceled-at"))
        order.finished_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("finished-at"))
        order.order_type = json_data.get_string("type")
        order.filled_amount = json_data.get_float_or_default("field-amount", json_data.get_float_or_default("filled-amount", 0))
        order.filled_cash_amount = json_data.get_float_or_default("field-cash-amount", json_data.get_float_or_default("filled-cash-amount", 0))
        order.filled_fees = json_data.get_float_or_default("field-fees", json_data.get_float_or_default("filled-fees", 0))
        order.account_type = account_type
        order.source = json_data.get_string("source")
        order.state = json_data.get_string("state")
        order.stop_price = json_data.get_float_or_default("stop-price", 0.0)
        order.operator = json_data.get_string_or_default("operator", "")
        order.next_time = json_data.get_string_or_default("next-time", "")
        return order



