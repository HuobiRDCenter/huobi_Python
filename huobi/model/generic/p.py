from huobi.constant import *

class P:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.weight = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "id")
        PrintBasic.print_basic(self.name, format_data + "name")
        PrintBasic.print_basic(self.weight, format_data + "weight")


