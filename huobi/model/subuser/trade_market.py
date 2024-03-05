
class TradeMarket:
    """
    The trade information with price and amount etc.

    :member
        subUid: sub user ID.
        accountType:
        activation: sub user account state for given accountType.
    """

    def __init__(self):
        self.sub_uid = ""
        self.account_type = ""
        self.activation = ""
        self.errCode = 0
        self.errMessage = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.sub_uid, format_data + "subUid")
        PrintBasic.print_basic(self.account_type, format_data + "accountType")
        PrintBasic.print_basic(self.activation, format_data + "activation")
