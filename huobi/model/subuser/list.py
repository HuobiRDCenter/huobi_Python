class List:

    def __init__(self):
        self.accountType = ""
        self.activation = ""
        self.transferrable = None
        self.accountIds = []

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accountType, format_data + "accountType")
        PrintBasic.print_basic(self.activation, format_data + "activation")
        PrintBasic.print_basic(self.transferrable, format_data + "transferrable")
        if self.accountIds and len(self.accountIds):
            for accountIds_obj in self.accountIds:
                accountIds_obj.print_object("\t")
                print()


