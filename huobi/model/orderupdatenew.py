from huobi.model.constant import *


class OrderUpdateNew:
    """
    The detail order information.

    :member
        match_id: The Match id for make order.
        order_id: The order id.
        symbol: The symbol, like "btcusdt".
        state: The order state: submitted, partial-filled, cancelling, filled, canceled.
        role: value is taker or maker
        price: The limit price of limit order.
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker, buy-limit-fok, sell-limit-fok.
        filled_amount: The amount which has been filled.
        filled_cash_amount: The filled total in quote currency.
        unfilled_amount: The amount which is unfilled.
    """

    def __init__(self):
        self.match_id = 0
        self.order_id = 0
        self.symbol = ""
        self.state = OrderState.INVALID
        self.role = ""
        self.price = 0.0
        self.filled_amount = 0.0
        self.filled_cash_amount = 0.0
        self.unfilled_amount = 0.0
        self.client_order_id = ""
        self.order_type = OrderType.INVALID

    @staticmethod
    def json_parse(json_data):
        order_upd = OrderUpdateNew()

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

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.match_id, format_data + "Match Id")
        PrintBasic.print_basic(self.order_id, format_data + "Order Id")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.state, format_data + "Order State")
        PrintBasic.print_basic(self.role, format_data + "Role")
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.filled_amount, format_data + "Filled Amount")
        PrintBasic.print_basic(self.filled_cash_amount, format_data + "Filled Cash Amount")
        PrintBasic.print_basic(self.unfilled_amount, format_data + "Unfilled Amount")
        PrintBasic.print_basic(self.client_order_id, format_data + "Client Order Id")
        PrintBasic.print_basic(self.order_type, format_data + "Order Type")



