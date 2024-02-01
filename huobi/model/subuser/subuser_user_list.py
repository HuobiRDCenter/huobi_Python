class SubuserUserList:
    def __init__(self):
        self.uid = 0
        self.userState = ""
        self.subUserName = ""
        self.note = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.uid, format_data + "uid")
        PrintBasic.print_basic(self.userState, format_data + "userState")
        PrintBasic.print_basic(self.subUserName, format_data + "subUserName")
        PrintBasic.print_basic(self.note, format_data + "note")

