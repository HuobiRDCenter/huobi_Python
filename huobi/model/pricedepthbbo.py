from huobi.model.depthentry import DepthEntry


class PriceDepthBbo:
    """
    The price depth information.

    :member
        timestamp: The UNIX formatted timestamp in UTC.
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.ask = 0.0
        self.ask_size = 0.0
        self.bid = 0.0
        self.bid_size = 0.0
        self.quote_time = 0
        self.symbol = ""

    @staticmethod
    def json_parse(json_data):
        bbo_obj = PriceDepthBbo()
        bbo_obj.ask = json_data.get_string("ask")
        bbo_obj.ask_size = json_data.get_float_at("askSize")
        bbo_obj.bid = json_data.get_string("bid")
        bbo_obj.bid_size = json_data.get_float_at("bidSize")
        bbo_obj.quote_time = json_data.get_string("quoteTime")
        bbo_obj.symbol = json_data.get_float_at("symbol")
        return bbo_obj
