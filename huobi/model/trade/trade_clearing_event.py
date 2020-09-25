from huobi.model.trade import TradeClearing


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
    def json_parse(data_json):
        event_obj = TradeClearingEvent()
        event_obj.action = data_json.get("action")
        event_obj.ch = data_json.get("ch")
        event_obj.seq = data_json.get("seq", 0)
        event_obj.data = TradeClearing.json_parse(data_json.get("data", {}))
        return event_obj

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        self.data.print_object()
