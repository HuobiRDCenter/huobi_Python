from huobi.model.constant import *


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


