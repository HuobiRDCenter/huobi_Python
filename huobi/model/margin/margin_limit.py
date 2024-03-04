from huobi.constant import *


class MarginLimit:

    def __init__(self):
        self.currency = ""
        self.max_holdings = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "currency")
        PrintBasic.print_basic(self.maxHoldings, format_data + "maxHoldings")





