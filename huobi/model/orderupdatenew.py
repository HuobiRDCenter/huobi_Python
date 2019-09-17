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
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker.
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




