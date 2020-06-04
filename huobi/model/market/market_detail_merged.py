
class MarketDetailMerged:
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
        self.amount = 0
        self.open = 0.0
        self.close = 0.0
        self.high = 0.0
        self.id = 0
        self.count = 0.0
        self.low = 0.0
        self.version = 0
        self.ask = []
        self.vol = 0.0
        self.bid = []

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        # PrintBasic.print_basic(self.version, format_data + "Version")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.count, format_data + "Count")
        PrintBasic.print_basic(self.vol, format_data + "Volume")

        PrintBasic.print_basic(self.open, format_data + "Open")
        PrintBasic.print_basic(self.close, format_data + "Close")
        PrintBasic.print_basic(self.high, format_data + "High")
        PrintBasic.print_basic(self.low, format_data + "Low")

        print("Ask", self.ask)
        print("Bid", self.bid)