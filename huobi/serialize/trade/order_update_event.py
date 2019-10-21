from huobi.utils.channel_parser import ChannelParser
from huobi.utils.time_service import convert_cst_in_millisecond_to_utc
from huobi.model.trade import *
from huobi.serialize.trade import *


class OrderUpdateEventSerial:
    @staticmethod
    def json_parse(json_data, account_type_map):
        ch = json_data.get_string("topic")
        parse = ChannelParser(ch)
        order_update_event = OrderUpdateEvent()
        order_update_event.symbol = parse.symbol
        order_update_event.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        data = json_data.get_object("data")
        account_id = data.get_int("account-id")
        order = OrderSerial.json_parse(data, account_type_map[account_id])
        order_update_event.data = order
        return order_update_event

