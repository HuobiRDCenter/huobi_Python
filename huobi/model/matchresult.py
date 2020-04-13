from huobi.model.constant import *


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
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit,
            buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker, buy-limit-fok, sell-limit-fok, buy-stop-limit-fok, sell-stop-limit-fok.
        filled_points: deduct points
        fee_deduct_currency: deduct type, it means deduct from HT/ HT points / or other currency
    """

    def __init__(self):
        self.created_timestamp = 0
        self.filled_amount = 0.0
        self.filled_fees = 0.0
        self.id = 0
        self.match_id = 0
        self.order_id = 0
        self.price = 0.0
        self.source = OrderSource.INVALID
        self.symbol = ""
        self.order_type = OrderType.INVALID
        self.role = ""
        self.filled_points = ""
        self.fee_deduct_currency = ""
