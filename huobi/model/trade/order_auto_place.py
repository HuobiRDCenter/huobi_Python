from huobi.constant import *
from huobi.utils.json_parser import fill_obj


class OrderAutoPlace:

    def __init__(self):
        self.order_id = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.order_id, format_data + "order_id")



