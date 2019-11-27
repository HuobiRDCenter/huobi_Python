from huobi.constant.result import OutputKey
from huobi.impl.utils.channelparser import ChannelParser
from huobi.model import Trade


class TradeRequest:
    """
    The trade received by subscription of trade.

    :member
        symbol: The symbol you subscribed.
        trade_list: The trade list. The content is Trade class.
    """

    def __init__(self):
        self.symbol = ""
        self.trade_list = list()

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelRep)
        parse = ChannelParser(ch)
        trade_event = TradeRequest()
        trade_event.symbol = parse.symbol
        tick = json_wrapper.get_array(OutputKey.KeyData)
        trade_list = list()
        for item in tick.get_items():
            trade = Trade.json_parse(item)  # others return trade-id, here return tradeId
            trade_list.append(trade)
        trade_event.trade_list = trade_list
        return trade_event

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, "Symbol")
        print()
        if len(self.trade_list):
            for trade in self.trade_list:
                trade.print_object()
                print()