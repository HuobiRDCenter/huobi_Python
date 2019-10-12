from huobi.constant.result import OutputKey
from huobi.utils.channelparser import ChannelParser
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import *


class PriceDepthEventSerial:


    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelCh)
        parse = ChannelParser(ch)
        price_depth_event = PriceDepthEvent()
        price_depth_event.symbol = parse.symbol
        price_depth_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
        price_depth_event.ch = ch
        data = json_wrapper.get_object(OutputKey.KeyTick)
        price_depth = PriceDepth.json_parse(data)
        price_depth_event.data = price_depth
        return price_depth_event


