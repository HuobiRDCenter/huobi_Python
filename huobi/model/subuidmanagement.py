from huobi.model import SubUidState


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

    @staticmethod
    def json_parse(json_data):
        obj = SubUidManagement()
        obj.subUid = json_data.get_int("subUid")
        obj.userState = json_data.get_string("userState")
        return obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.subUid, format_data + "subUid")
        PrintBasic.print_basic(self.userState, format_data + "userState")