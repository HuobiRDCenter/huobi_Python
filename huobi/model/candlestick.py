class Candlestick:
    """
    The candlestick/kline data.

    :member
        timestamp: The UNIX formatted timestamp in UTC.
        high: The high price.
        low: The low price.
        open: The opening price.
        close: The closing price.
        amount: The aggregated trading volume in USDT.
        count: The number of completed trades. it returns 0 when get ETF candlestick
        volume: The trading volume in base currency.

    """

    def __init__(self):
        self.timestamp = 0
        self.high = 0.0
        self.low = 0.0
        self.open = 0.0
        self.close = 0.0
        self.amount = 0.0
        self.count = 0
        self.volume = 0.0
