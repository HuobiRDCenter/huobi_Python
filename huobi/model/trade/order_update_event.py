from huobi.model.trade.order_update import OrderUpdate


class OrderUpdateEvent:
    """
    The order update received by subscription of order update.

    :member
        ch: The symbol you subscribed.
        data: The order detail.

    """

    def __init__(self):
        self.ch = ""
        self.data = OrderUpdate()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Topic")

        orderupdate = self.data
        orderupdate.print_object()