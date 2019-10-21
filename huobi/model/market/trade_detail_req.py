

class TradeDetailReq:
    """
    The trade received by subscription of trade.

    :member
        rep: The Channel you subscribed.
        trade_list: The trade list. The content is Trade class.
    """

    def __init__(self):
        self.rep = ""
        self.data = list()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.rep, format_data + "Channel")
        print()
        if len(self.data):
            for trade_detail in self.data:
                trade_detail.print_object()
                print()