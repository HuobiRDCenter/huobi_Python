from huobi.utils.channelparser import ChannelParser
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import *



class OrderUpdateEventV2Serial:

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string("topic")
        parse = ChannelParser(ch)
        order_update_event = OrderUpdateEventV2()
        order_update_event.symbol = parse.symbol
        order_update_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
        data = json_wrapper.get_object("data")
        order = OrderUpdateV2.json_parse(data)

        order_update_event.data = order
        return order_update_event

