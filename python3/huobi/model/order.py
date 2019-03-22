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
        order_type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker.
        filled_amount: The amount which has been filled.
        filled_cash_amount: The filled total in quote currency.
        filled_fees: The transaction fee paid so far.
        source: The source where the order was triggered, possible values: sys, web, api, app.
        state: The order state: submitted, partial-filled, cancelling, filled, canceled.
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
