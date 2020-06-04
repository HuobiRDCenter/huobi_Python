class MarketTicker:
    """
    The ticker information.

    :member
        amount: The aggregated trading volume in last 24 hours (rotating 24h).
        count: The number of completed trades of last 24 hours (rotating 24h).
        open: The opening price of a nature day (Singapore time).
        close: The last price of a nature day (Singapore time).
        low: The low price of a nature day (Singapore time).
        high: The high price of a nature day (Singapore time).
        vol: The aggregated trading value in last 24 hours (rotating 24h).
        symbol: The trading symbol of this object, e.g. btcusdt, bccbtc.
        bid: Best bid price.
        bidSize: Best bid size.
        ask: Best ask price.
        askSize: Best ask size.
    """

    def __init__(self):
        self.amount = 0.0
        self.count = 0
        self.open = 0.0
        self.close = 0.0
        self.low = 0.0
        self.high = 0.0
        self.vol = 0.0
        self.symbol = ""
        self.bid = 0.0
        self.bidSize = 0.0
        self.ask = 0.0
        self.askSize = 0.0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.count, format_data + "Count")
        PrintBasic.print_basic(self.open, format_data + "Opening Price")
        PrintBasic.print_basic(self.close, format_data + "Last Price")
        PrintBasic.print_basic(self.low, format_data + "Low Price")
        PrintBasic.print_basic(self.high, format_data + "High Price")
        PrintBasic.print_basic(self.vol, format_data + "Vol")
        PrintBasic.print_basic(self.symbol, format_data + "Trading Symbol")
        PrintBasic.print_basic(self.bid, format_data + "Best Bid Price")
        PrintBasic.print_basic(self.bidSize, format_data + "Best Bid Size")
        PrintBasic.print_basic(self.ask, format_data + "Best Ask Price")
        PrintBasic.print_basic(self.askSize, format_data + "Best Ask Size")