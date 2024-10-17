
class FeeRate:
    """
    The account information for spot account, margin account etc.

    :member
        symbol: The symbol, like "btcusdt".
        maker_fee: maker fee rate
        taker_fee: taker fee rate

    """

    def __init__(self):
        self.symbol = ""
        self.maker_fee = ""
        self.taker_fee = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.maker_fee, format_data + "Maker Fee")
        PrintBasic.print_basic(self.taker_fee, format_data + "Taker Fee")