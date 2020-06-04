from huobi.constant import SubUidState


class SubUidManagement:
    """
    The trade information with price and amount etc.

    :member
        subUid: sub user ID.
        userState: sub user account state, states see SubUidState.
    """

    def __init__(self):
        self.subUid = 0
        self.userState = SubUidState.INVALID

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.subUid, format_data + "subUid")
        PrintBasic.print_basic(self.userState, format_data + "userState")
