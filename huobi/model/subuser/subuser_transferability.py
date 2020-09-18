
class SubuserTransferability:
    """
    The trade information with price and amount etc.

    :member
        subUid: sub user ID.
        userState: sub user account state, states see SubUidState.
    """

    def __init__(self):
        self.transferrable = ""
        self.accountType = ""
        self.subUid = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.subUid, format_data + "subUid")
        PrintBasic.print_basic(self.accountType, format_data + "accountType")
        PrintBasic.print_basic(self.transferrable, format_data + "transferrable")
