from huobi.constant.result import OutputKey
from huobi.utils.channelparser import ChannelParser
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import Trade


class TradeReqSerial:

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelRep)
        parse = ChannelParser(ch)
        trade_event = TradeRequest()
        trade_event.symbol = parse.symbol
        tick = json_wrapper.get_array(OutputKey.KeyData)
        trade_list = list()
        for item in tick.get_items():
            trade = Trade.json_parse(item)
            trade_list.append(trade)
        trade_event.trade_list = trade_list
        return trade_event

