from huobi.constant.result import OutputKey
from huobi.utils import *
from huobi.utils.channelparser import ChannelParser
from huobi.constant import *
from huobi.model.market import *


class CandlestickReqSerial:

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelRep)
        parse = ChannelParser(ch)
        candlestick_event = CandlestickRequest()
        candlestick_event.symbol = parse.symbol
        candlestick_event.interval = ""
        tick = json_wrapper.get_array(OutputKey.KeyData)
        candlestick_list = list()
        for item in tick.get_items():
            data = Candlestick.json_parse(item)
            candlestick_list.append(data)

        candlestick_event.data = candlestick_list
        return candlestick_event

