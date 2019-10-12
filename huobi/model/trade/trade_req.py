

class TradeReq:
    """
    The trade received by subscription of trade.

    :member
        symbol: The symbol you subscribed.
        trade_list: The trade list. The content is Trade class.
    """

    def __init__(self):
        self.symbol = ""
        self.trade_list = list()

    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        print()
        if len(self.trade_list):
            for trade in self.trade_list:
                trade.print_object()
                print()