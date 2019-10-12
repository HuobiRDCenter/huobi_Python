
class BestQuote:
    """
    The best bid/ask consisting of price and amount.

    :member
        timestamp: The Unix formatted timestamp in UTC.
        bid_price: The best bid price.
        bid_amount: The best bid amount.
        ask_price: The best ask price.
        ask_amount: The best ask amount.

    """

    def __init__(self):
        self.timestamp = 0
        self.bid_price = 0.0
        self.bid_amount = 0.0
        self.ask_price = 0.0
        self.ask_amount = 0.0

    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.timestamp, format_data + "Timestamp")
        PrintBasic.print_basic(self.bid_price, format_data + "Bid Price")
        PrintBasic.print_basic(self.bid_amount, format_data + "Bid Amount")
        PrintBasic.print_basic(self.ask_price, format_data + "Ask Price")
        PrintBasic.print_basic(self.ask_amount, format_data + "Ask Amount")