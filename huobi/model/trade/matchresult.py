from huobi.constant import *


class MatchResult:
    """
    The match result information.

    :member
        created_timestamp: The UNIX formatted timestamp in UTC when the match and fill is done.
        filled_amount: The amount which has been filled.
        filled_fees: The transaction fee paid so far.
        id: The internal id.
        match_id: The match id of this match.
        order_id: The order id of this order.
        price: The limit price of limit order.
        source: The source where the order was triggered, possible values: sys, web, api, app.
        symbol: The symbol, like "btcusdt".
        type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit,
            buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker, buy-limit-fok, sell-limit-fok, buy-stop-limit-fok, sell-stop-limit-fok.
        filled_points: deduct points
        fee_deduct_currency: deduct type, it means deduct from HT/ HT points / or other currency
        fee_currency:
    """

    def __init__(self):
        self.created_at = 0
        self.filled_amount = 0.0
        self.filled_fees = 0.0
        self.id = 0
        self.match_id = 0
        self.order_id = 0
        self.price = 0.0
        self.source = OrderSource.INVALID
        self.symbol = ""
        self.type = OrderType.INVALID
        self.role = ""
        self.filled_points = ""
        self.fee_deduct_currency = ""
        self.fee_currency = ""
        self.fee_deduct_state = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.created_at, format_data + "Create Time")
        PrintBasic.print_basic(self.filled_amount, format_data + "Fill Amount")
        PrintBasic.print_basic(self.filled_fees, format_data + "Fill Fee")
        PrintBasic.print_basic(self.filled_points, format_data + "Fill Points")
        PrintBasic.print_basic(self.match_id, format_data + "Match ID")
        PrintBasic.print_basic(self.order_id, format_data + "Order ID")
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.source, format_data + "Source")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.type, format_data + "Order Type")
        PrintBasic.print_basic(self.role, format_data + "Role")
        PrintBasic.print_basic(self.fee_deduct_currency, format_data + "Fee Deduct Currency")
        PrintBasic.print_basic(self.fee_currency, format_data + "Fee Currency")
        PrintBasic.print_basic(self.fee_deduct_state, format_data + "Fee Deduct State")
