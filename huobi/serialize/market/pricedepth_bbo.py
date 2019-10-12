


class PriceDepthBboSerial:

    @staticmethod
    def json_parse(json_data):
        bbo_obj = PriceDepthBbo()
        bbo_obj.ask = json_data.get_string("ask")
        bbo_obj.ask_size = json_data.get_string("askSize")
        bbo_obj.bid = json_data.get_string("bid")
        bbo_obj.bid_size = json_data.get_string("bidSize")
        bbo_obj.quote_time = json_data.get_string("quoteTime")
        bbo_obj.symbol = json_data.get_string("symbol")
        return bbo_obj


