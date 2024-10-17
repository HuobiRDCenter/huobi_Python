from huobi.constant import *
from huobi.utils import default_parse_list_dict


class Updated:

    def __init__(self):
        self.success = None
        self.time = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.success, format_data + "success")
        PrintBasic.print_basic(self.time, format_data + "time")


