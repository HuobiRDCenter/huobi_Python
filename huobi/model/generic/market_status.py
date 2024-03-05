from huobi.constant import *


class MarketStatus:
    """
    The Huobi market status info.

    :member
        marketStatus: .
        haltStartTime: .
        haltEndTime: .
        haltReason:
        affectedSymbols:
    """

    def __init__(self):
        self.marketStatus = MarketStatus.NORMAL
        self.haltStartTime = -1
        self.haltEndTime = -1
        self.haltReason = -1
        self.affectedSymbols = ""
