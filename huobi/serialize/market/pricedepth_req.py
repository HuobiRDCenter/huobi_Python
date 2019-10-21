
from huobi.model.market import *
from huobi.serialize.market import *


class PriceDepthReqSerial:


    @staticmethod
    def json_parse(dict_data):
        price_depth_event = PriceDepthReq()
        price_depth_event.id = dict_data.get("id")
        price_depth_event.rep = dict_data.get("rep")
        data = dict_data.get("data", {})
        price_depth_obj = PriceDepthSerial.json_parse_pricedepth(data)
        price_depth_event.data = price_depth_obj
        return price_depth_event





