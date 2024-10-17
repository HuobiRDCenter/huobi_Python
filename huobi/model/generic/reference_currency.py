from huobi.constant import *

class ReferenceCurrency:
    """
    The Huobi supported static reference information for each currency.

    :member
        currency: currency
        instStatus: Instrument status
        chains: chain list
    """

    def __init__(self):
        self.currency = ""
        self.instStatus = InstrumentStatus.INVALID
        self.chains = []


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.instStatus, format_data + "Instrument Status")
        if self.chains and len(self.chains):
            for chain_obj in self.chains:
                chain_obj.print_object("\t")
                print()
