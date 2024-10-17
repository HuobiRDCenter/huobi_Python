class MarketDetail:
    """
    The summary of trading in the market for the last 24 hours

    :member
        id: response ID
        open: The opening price of last 24 hours.
        close: The last price of last 24 hours.
        amount: The aggregated trading volume in USDT.
        high: The high price of last 24 hours.
        low: The low price of last 24 hours.
        count: The number of completed trades.
        volume: The trading volume in base currency of last 24 hours.
        version: inner data
    """

    def __init__(self):
        self.id = 0
        self.open = 0.0
        self.close = 0.0
        self.amount = 0.0
        self.high = 0.0
        self.low = 0.0
        self.count = 0
        self.vol = 0.0
        self.version = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.open, format_data + "Open")
        PrintBasic.print_basic(self.close, format_data + "Close")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.high, format_data + "High")
        PrintBasic.print_basic(self.low, format_data + "Low")
        PrintBasic.print_basic(self.count, format_data + "Count")
        PrintBasic.print_basic(self.vol, format_data + "Volume")
        # PrintBasic.print_basic(self.version, format_data + "Version")