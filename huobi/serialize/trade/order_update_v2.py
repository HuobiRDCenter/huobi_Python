from huobi.constant import *


class OrderUpdateV2Serial:


    @staticmethod
    def json_parse(json_data):
        order_upd = OrderUpdateV2()

        order_upd.match_id = json_data.get_int("match-id")
        order_upd.order_id = json_data.get_int("order-id")
        order_upd.symbol = json_data.get_string("symbol")
        order_upd.state = json_data.get_string("order-state")
        order_upd.role = json_data.get_string("role")
        order_upd.price = json_data.get_float("price")
        order_upd.order_type = json_data.get_string("order-type")
        order_upd.filled_amount = json_data.get_float("filled-amount")
        order_upd.filled_cash_amount = json_data.get_float("filled-cash-amount")
        order_upd.unfilled_amount = json_data.get_float("unfilled-amount")
        order_upd.client_order_id = json_data.get_string("client-order-id")

        return order_upd





