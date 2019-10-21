from huobi.constant import *


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
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker.
        filled_amount: The amount which has been filled.
        filled_cash_amount: The filled total in quote currency.
        filled_fees: The transaction fee paid so far.
        source: The source where the order was triggered, possible values: sys, web, api, app.
        state: The order state: submitted, partial-filled, cancelling, filled, canceled.
        stop_price : stop price used for buy-stop-limit，sell-stop-limit
        operator : only [gte] and [lte] to trigger buy-stop-limit，sell-stop-limit
    """

    def __init__(self):
        self.id = 0
        self.symbol = ""
        self.account_id = 0
        #self.account_type = AccountType.INVALID

        self.amount = 0.0
        self.price = 0.0
        self.created_at = 0
        self.canceled_at = 0
        self.finished_at = 0
        self.id = 0
        self.symbol = ""
        self.type = OrderType.INVALID
        self.field_amount = 0.0
        self.field_cash_amount = 0.0
        self.field_fees = 0.0
        self.source = OrderSource.INVALID
        self.state = OrderState.INVALID
        self.stop_price = ""
        self.next_time = 0
        self.operator=""

 
    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Order Id")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.created_at, format_data + "Create Time")
        PrintBasic.print_basic(self.canceled_at, format_data + "Cancel Time")
        PrintBasic.print_basic(self.finished_at, format_data + "Finish Time")
        PrintBasic.print_basic(self.type, format_data + "Order Type")
        PrintBasic.print_basic(self.field_amount, format_data + "Field Amount")
        PrintBasic.print_basic(self.field_cash_amount, format_data + "Field Cash Amount")
        PrintBasic.print_basic(self.field_fees, format_data + "Field Fees")
        #PrintBasic.print_basic(self.account_type, format_data + "Account Type")
        PrintBasic.print_basic(self.source, format_data + "Order Source")
        PrintBasic.print_basic(self.state, format_data + "Order State")
        PrintBasic.print_basic(self.stop_price, format_data + "Stop Price")
        PrintBasic.print_basic(self.operator, format_data + "Operator")
        PrintBasic.print_basic(self.next_time, format_data + "Next Time")

