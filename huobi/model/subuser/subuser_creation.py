
class SubuserCreation:
    """
    The trade information with price and amount etc.

    :member
        subUid: sub user ID.
        userState: sub user account state, states see SubUidState.
    """

    def __init__(self):
        self.userName = ""
        self.note = ""
        self.uid = 0
        self.errCode = 0
        self.errMessage = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.user_name, format_data + "userName")
        PrintBasic.print_basic(self.note, format_data + "note")
        PrintBasic.print_basic(self.uid, format_data + "uid")
        PrintBasic.print_basic(self.err_code, format_data + "errCode")
        PrintBasic.print_basic(self.err_message, format_data + "errMessage")



