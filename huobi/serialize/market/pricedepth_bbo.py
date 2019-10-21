from huobi.model.market import *

class PriceDepthBboSerial:

    @staticmethod
    def json_parse(dict_data):
        bbo_obj = PriceDepthBbo()
        bbo_obj.ask = dict_data.get("seqId")
        bbo_obj.ask = dict_data.get("ask")
        bbo_obj.ask_size = dict_data.get("askSize")
        bbo_obj.bid = dict_data.get("bid")
        bbo_obj.bid_size = dict_data.get("bidSize")
        bbo_obj.quote_time = dict_data.get("quoteTime")
        bbo_obj.symbol = dict_data.get("symbol")
        return bbo_obj


