
class Candlestick:
    """
    The candlestick/kline data.

    :member
        id : keep the original timestamp
        high: The high price.
        low: The low price.
        open: The opening price.
        close: The closing price.
        amount: The aggregated trading volume in USDT.
        count: The number of completed trades. it returns 0 when get ETF candlestick
        volume: The trading volume in base currency.

    """

    def __init__(self):
        self.id = 0
        self.high = 0.0
        self.low = 0.0
        self.open = 0.0
        self.close = 0.0
        self.amount = 0.0
        self.count = 0
        self.volume = 0.0

    @staticmethod
    def json_parse(json_data):
        data_obj = Candlestick()
        data_obj.id = json_data.get_int("id")
        data_obj.open = json_data.get_float("open")
        data_obj.close = json_data.get_float("close")
        data_obj.low = json_data.get_float("low")
        data_obj.high = json_data.get_float("high")
        data_obj.amount = json_data.get_float("amount")
        data_obj.count = json_data.get_int("count")
        data_obj.volume = json_data.get_float("vol")
        return data_obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Id")
        PrintBasic.print_basic(self.high, format_data + "High")
        PrintBasic.print_basic(self.low, format_data + "Low")
        PrintBasic.print_basic(self.open, format_data + "Open")
        PrintBasic.print_basic(self.close, format_data + "Close")
        PrintBasic.print_basic(self.count, format_data + "Count")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.volume, format_data + "Volume")