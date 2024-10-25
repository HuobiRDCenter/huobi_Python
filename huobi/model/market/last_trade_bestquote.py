class LastTradeAndBestQuote:
    """
    The last trade and best bid/ask.

    :member
        last_trade_price: The last trade price.
        last_trade_amount: The last trade amount.
        ask_price: The best ask price.
        ask_amount: The best ask amount.
        bid_price: The best bid price.
        bid_amount: The best bid amount.

    """

    def __init__(self):
        self.last_trade_price = 0.0
        self.last_trade_amount = 0.0
        self.ask_price = 0.0
        self.ask_amount = 0.0
        self.bid_price = 0.0
        self.bid_amount = 0.0
