
class PriceDepthBbo:
    """
    The price depth information.

    :member
        timestamp: The UNIX formatted timestamp in UTC.
        bid: the first bid near trade value.
        bidSize: the bid size.
        ask: The first ask near trade value.
        askSize: the ask size.
        quoteTime : quote time
        symbol : trade symbol


    """
    def __init__(self):
        self.seqId = 0
        self.ask = 0.0
        self.askSize = 0.0
        self.bid = 0.0
        self.bidSize = 0.0
        self.quoteTime = 0
        self.symbol = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.seqId, format_data + "Seq ID")
        PrintBasic.print_basic(self.ask, format_data + "Ask")
        PrintBasic.print_basic(self.askSize, format_data + "Ask Size")
        PrintBasic.print_basic(self.bid, format_data + "Bid")
        PrintBasic.print_basic(self.bidSize, format_data + "Bid Size")
        PrintBasic.print_basic(self.quoteTime, format_data + "Quote Time")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")