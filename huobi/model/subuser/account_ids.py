class AccountIds:

    def __init__(self):
        self.accountId = ""
        self.subType = ""
        self.accountStatus = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accountId, format_data + "accountId")
        PrintBasic.print_basic(self.subType, format_data + "subType")
        PrintBasic.print_basic(self.accountStatus, format_data + "accountStatus")



