from huobi.model.tradeclearing import TradeClearing


class TradeClearingEvent:
    """
    subscribe trading clearing information

    :member
        action: current is "sub" for subscribe
        ch: subscribe topic.
        data: data detail in TradeClearing.
    """
    def __init__(self):
        self.action = ""
        self.ch = ""
        self.seq = 0
        self.data = TradeClearing()

    @staticmethod
    def json_parse(json_wrapper):
        event_obj = TradeClearingEvent()
        event_obj.action = json_wrapper.get_string("action")
        event_obj.ch = json_wrapper.get_string("ch")
        event_obj.seq = json_wrapper.get_int_or_default("seq", 0)
        event_obj.data = TradeClearing.json_parse(json_wrapper.get_object_or_default("data", {}))
        return event_obj


    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        self.data.print_object()