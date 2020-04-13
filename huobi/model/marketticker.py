

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

    @staticmethod
    def json_parse(json_data):
        market_ticker = MarketTicker()
        market_ticker.amount = json_data.get_float("amount")
        market_ticker.count = json_data.get_int("count")
        market_ticker.open = json_data.get_float("open")
        market_ticker.close = json_data.get_float("close")
        market_ticker.low = json_data.get_float("low")
        market_ticker.high = json_data.get_float("high")
        market_ticker.vol = json_data.get_float("vol")
        market_ticker.symbol = json_data.get_string("symbol")
        market_ticker.bid = json_data.get_float("bid")
        market_ticker.bidSize = json_data.get_float("bidSize")
        market_ticker.ask = json_data.get_float("ask")
        market_ticker.askSize = json_data.get_float("askSize")
        return market_ticker

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
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
