from huobi.constant.result import OutputKey
from huobi.impl.utils.channelparser import ChannelParser
from huobi.model import Mbp
from huobi.model.ordersupdate import OrdersUpdate


class OrdersUpdateEvent:
    """
    The order update received by subscription of order update.

    """

    def __init__(self):
        self.action = ""
        self.code = 200
        self.ch = ""
        self.data = OrdersUpdate()

    @staticmethod
    def json_parse(json_wrapper):
        action = json_wrapper.get_string(OutputKey.KeyAction)
        ch = json_wrapper.get_string(OutputKey.KeyChannelCh)
        data = json_wrapper.get_object(OutputKey.KeyData)

        order_update_v2_event = OrdersUpdateEvent()
        order_update_v2_event.action = action
        order_update_v2_event.ch = ch
        order_update_v2_event.data = OrdersUpdate.json_parse(data)
        return order_update_v2_event

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        self.data.print_object()
