from huobi.model.market import *
from huobi.serialize.market import *
from huobi.utils import *


class PriceDepthSerial:

    @staticmethod
    def get_depth_step_list():
        return [DepthStep.STEP0,
                DepthStep.STEP1,
                DepthStep.STEP2,
                DepthStep.STEP3,
                DepthStep.STEP4,
                DepthStep.STEP5]

    @staticmethod
    def get_valid_depth_step(value, defalut_value):
        step_list = PriceDepthSerial.get_depth_step_list()
        if value in step_list:
            return value
        else:
            return defalut_value

    @staticmethod
    def json_parse(dict_data):
        tick = dict_data.get("tick", {})
        price_depth = PriceDepthSerial.json_parse_pricedepth(tick)
        return price_depth

    @staticmethod
    def json_parse_pricedepth(dict_data):
        price_depth_obj = PriceDepth()
        price_depth_obj.ts = dict_data.get("ts")
        price_depth_obj.version = dict_data.get("version")
        bid_list = list()
        bids_array = dict_data.get("bids", [])
        for item in bids_array:
            depth_entry = DepthEntrySerial.json_parse(item)
            bid_list.append(depth_entry)
        ask_list = list()
        asks_array = dict_data.get("asks", [])
        for item in asks_array:
            depth_entry = DepthEntrySerial.json_parse(item)
            ask_list.append(depth_entry)
        price_depth_obj.bids = bid_list
        price_depth_obj.asks = ask_list

        return price_depth_obj
