class AccountAssetValuationResult:
    """
    The account information for spot account, margin account etc.

    :member
        balance: balance valuation bases on given valuation currency.
        timestamp: unix timestamp from server.

    """

    def __init__(self):
        self.balance = ""
        self.timestamp = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.balance, format_data + "balance")
        PrintBasic.print_basic(self.timestamp, format_data + "timestamp")
