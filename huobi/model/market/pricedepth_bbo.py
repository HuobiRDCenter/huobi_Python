
class PriceDepthBbo:
    """
    The price depth information.

    :member
        timestamp: The UNIX formatted timestamp in UTC.
        bid: the first bid near trade value.
        bid_size: the bid size.
        ask: The first ask near trade value.
        ask_size: the ask size.
        quote_time : quote time
        symbol : trade symbol


    """
    def __init__(self):
        self.seq_id = 0
        self.ask = 0.0
        self.ask_size = 0.0
        self.bid = 0.0
        self.bid_size = 0.0
        self.quote_time = 0
        self.symbol = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.seq_id, format_data + "Seq ID")
        PrintBasic.print_basic(self.ask, format_data + "Ask")
        PrintBasic.print_basic(self.ask_size, format_data + "Ask Size")
        PrintBasic.print_basic(self.bid, format_data + "Bid")
        PrintBasic.print_basic(self.bid_size, format_data + "Bid Size")
        PrintBasic.print_basic(self.quote_time, format_data + "Quote Time")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")