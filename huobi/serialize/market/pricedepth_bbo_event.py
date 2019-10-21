from huobi.constant.result import OutputKey
from huobi.utils.channel_parser import ChannelParser
from huobi.utils.time_service import convert_cst_in_millisecond_to_utc
from huobi.model.market import *
from huobi.serialize.market import *


class PriceDepthBboEventSerial:

    @staticmethod
    def json_parse(dict_data):
        price_depth_event = PriceDepthBboEvent()
        price_depth_event.ch = dict_data.get("ch", "")
        price_depth_event.ts = convert_cst_in_millisecond_to_utc(dict_data.get("ts"))
        tick = dict_data.get("tick", {})
        price_depth = PriceDepthBboSerial.json_parse(tick)
        price_depth_event.tick = price_depth
        return price_depth_event


