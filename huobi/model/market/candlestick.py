
class Candlestick:
    """
    The candlestick/kline data.

    :member
        id : keep the original timestamp
        timestamp: The UNIX formatted timestamp in UTC.
        high: The high price.
        low: The low price.
        open: The opening price.
        close: The closing price.
        amount: The aggregated trading volume in USDT.
        count: The number of completed trades. it returns 0 when get ETF candlestick
        vol: The trading volume in base currency.

    """

    def __init__(self):
        self.id = 0
        #self.timestamp = 0
        self.high = 0.0
        self.low = 0.0
        self.open = 0.0
        self.close = 0.0
        self.amount = 0.0
        self.count = 0
        self.vol = 0.0  #self.volume = 0.0


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Id")
        #PrintBasic.print_basic(self.timestamp, format_data + "Unix Time")
        PrintBasic.print_basic(self.high, format_data + "High")
        PrintBasic.print_basic(self.low, format_data + "Low")
        PrintBasic.print_basic(self.open, format_data + "Open")
        PrintBasic.print_basic(self.close, format_data + "Close")
        PrintBasic.print_basic(self.count, format_data + "Count")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.vol, format_data + "Volume")