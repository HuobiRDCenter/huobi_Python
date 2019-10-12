class UnitPrice:

    def __init__(self):
        self.currency = ""
        self.amount = 0.0

    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.amount, format_data + "Amount")