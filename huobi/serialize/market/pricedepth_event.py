from huobi.utils.time_service import convert_cst_in_millisecond_to_utc
from huobi.model.market import *
from huobi.serialize.market.pricedepth import PriceDepthSerial



class PriceDepthEventSerial:

    @staticmethod
    def json_parse(dict_data):

        price_depth_event = PriceDepthEvent()
        price_depth_event.ch = dict_data.get("ch")
        tick = dict_data.get("tick", {})
        price_depth_obj = PriceDepthSerial.json_parse_pricedepth(tick)
        price_depth_event.data = price_depth_obj
        return price_depth_event


