class SubuserAccountList:

    def __init__(self):
        self.uid = 0
        self.deductMode = ""
        self.list = []

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.uid, format_data + "uid")
        PrintBasic.print_basic(self.deductMode, format_data + "deductMode")
        if self.list and len(self.list):
            for list_obj in self.list:
                list_obj.print_object("\t")
                print()


