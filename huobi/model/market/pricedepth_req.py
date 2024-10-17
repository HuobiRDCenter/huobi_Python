
from huobi.model.market.pricedepth import PriceDepth

class PriceDepthReq:
    """
    The price depth information.

    :member
        ts: The UNIX formatted timestamp in UTC.
        version:
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.rep = ""
        self.data = PriceDepth()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.rep, format_data + "Channel")
        self.data.print_object("\t")