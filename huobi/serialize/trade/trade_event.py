from huobi.utils.channelparser import ChannelParser
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import Trade


class TradeEventSerial:

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string("ch")
        parse = ChannelParser(ch)
        trade_event = TradeEvent()
        trade_event.symbol = parse.symbol
        trade_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
        tick = json_wrapper.get_object("tick")
        data_array = tick.get_array("data")
        trade_list = list()
        for item in data_array.get_items():
            trade = Trade.json_parse(item)
            trade_list.append(trade)
        trade_event.trade_list = trade_list
        return trade_event

