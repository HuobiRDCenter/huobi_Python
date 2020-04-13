from huobi.model.constant import *


class Order:
    """
    The detail order information.

    :member
        account_type: The account type which created this order.
        amount: The amount of base currency in this order.
        price: The limit price of limit order.
        created_timestamp: The UNIX formatted timestamp in UTC when the order was created.
        canceled_timestamp: The UNIX formatted timestamp in UTC when the order was canceled, if not canceled then has value of 0.
        finished_timestamp: The UNIX formatted timestamp in UTC when the order was changed to a final state. This is not the time the order is matched.
        order_id: The order id.
        symbol: The symbol, like "btcusdt".
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker, buy-limit-fok, sell-limit-fok, buy-stop-limit-fok, sell-stop-limit-fok.
        filled_amount: The amount which has been filled.
        filled_cash_amount: The filled total in quote currency.
        filled_fees: The transaction fee paid so far.
        source: The source where the order was triggered, possible values: sys, web, api, app.
        state: The order state: submitted, partial-filled, cancelling, filled, canceled.
        stop_price : stop price used for buy-stop-limit，sell-stop-limit
        operator : only [gte] and [lte] to trigger buy-stop-limit，sell-stop-limit
    """

    def __init__(self):
        self.account_type = AccountType.INVALID
        self.amount = 0.0
        self.price = 0.0
        self.created_timestamp = 0
        self.canceled_timestamp = 0
        self.finished_timestamp = 0
        self.order_id = 0
        self.symbol = ""
        self.order_type = OrderType.INVALID
        self.filled_amount = 0.0
        self.filled_cash_amount = 0.0
        self.filled_fees = 0.0
        self.source = OrderSource.INVALID
        self.state = OrderState.INVALID
        self.client_order_id = ""
        self.stop_price = ""
        self.next_time = 0
        self.operator=""

    @staticmethod
    def json_parse(json_data, account_type):
        order = Order()
        order.order_id = json_data.get_int("id")
        order.symbol = json_data.get_string("symbol")
        order.price = json_data.get_float("price")
        order.amount = json_data.get_float("amount")
        order.created_timestamp = json_data.get_int("created-at")
        order.canceled_timestamp = json_data.get_int_or_default("canceled-at", 0)
        order.finished_timestamp = json_data.get_int_or_default("finished-at", 0)
        order.order_type = json_data.get_string("type")
        order.filled_amount = json_data.get_float_or_default("field-amount", json_data.get_float_or_default("filled-amount", 0))
        order.filled_cash_amount = json_data.get_float_or_default("field-cash-amount", json_data.get_float_or_default("filled-cash-amount", 0))
        order.filled_fees = json_data.get_float_or_default("field-fees", json_data.get_float_or_default("filled-fees", 0))
        order.account_type = account_type
        order.source = json_data.get_string("source")
        order.state = json_data.get_string("state")
        order.client_order_id = json_data.get_string_or_default("client-order-id", "")
        order.stop_price = json_data.get_float_or_default("stop-price", 0.0)
        order.operator = json_data.get_string_or_default("operator", "")
        order.next_time = json_data.get_string_or_default("next-time", "")
        return order

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.order_id, format_data + "Order Id")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.created_timestamp, format_data + "Create Time")
        PrintBasic.print_basic(self.canceled_timestamp, format_data + "Cancel Time")
        PrintBasic.print_basic(self.finished_timestamp, format_data + "Finish Time")
        PrintBasic.print_basic(self.order_type, format_data + "Order Type")
        PrintBasic.print_basic(self.filled_amount, format_data + "Filled Amount")
        PrintBasic.print_basic(self.filled_cash_amount, format_data + "Filled Cash Amount")
        PrintBasic.print_basic(self.filled_fees, format_data + "Filled Fees")
        PrintBasic.print_basic(self.account_type, format_data + "Account Type")
        PrintBasic.print_basic(self.source, format_data + "Order Source")
        PrintBasic.print_basic(self.state, format_data + "Order State")
        PrintBasic.print_basic(self.client_order_id, format_data + "Client Order Id")
        PrintBasic.print_basic(self.stop_price, format_data + "Stop Price")
        PrintBasic.print_basic(self.operator, format_data + "Operator")
        PrintBasic.print_basic(self.next_time, format_data + "Next Time")


