
from huobi.model.market.pricedepth import PriceDepth
class PriceDepthEvent:
    """
    The price depth information.

    :member
        ts: The UNIX formatted timestamp in UTC.
        version:
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.ch = ""
        self.tick = PriceDepth()



    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        self.tick.print_object("\t")