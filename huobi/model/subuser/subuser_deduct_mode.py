class SubuserDeductMode:

    def __init__(self):
        self.subUid = ""
        self.deductMode = ""
        self.errCode = ""
        self.errMessage = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.subUid, format_data + "subUid")
        PrintBasic.print_basic(self.deductMode, format_data + "deductMode")
        PrintBasic.print_basic(self.errCode, format_data + "errCode")
        PrintBasic.print_basic(self.errMessage, format_data + "errMessage")


