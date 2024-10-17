
class TransactFeeRate:
    """
    The transact fee rate.

    :member
        symbol: symbol like "btcusdt"
        makerFeeRate: maker fee rate
        takerFeeRate: taker fee rate
        actualMakerRate: actual maker fee rate
        actualTakerRate: actual taker fee rate
    """

    def __init__(self):
        self.symbol = ""
        self.makerFeeRate = ""
        self.takerFeeRate = ""
        self.actualMakerRate = ""
        self.actualTakerRate = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.makerFeeRate, format_data + "makerFeeRate")
        PrintBasic.print_basic(self.takerFeeRate, format_data + "takerFeeRate")
        PrintBasic.print_basic(self.actualMakerRate, format_data + "actualMakerRate")
        PrintBasic.print_basic(self.actualTakerRate, format_data + "actualTakerRate")