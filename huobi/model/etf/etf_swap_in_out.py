

class EtfSwapInOut:
    """
    :member
    """

    def __init__(self):
        self.code = 0
        self.data = None
        self.message = ""
        self.success = False

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.code, format_data + "Return Code")
        PrintBasic.print_basic_bool(self.data, format_data + "Data")
        PrintBasic.print_basic(self.message, format_data + "Message")
        PrintBasic.print_basic_bool(self.success, format_data + "Success")
