
class DepthEntry:
    """
    An depth entry consisting of price and amount.

    :member
        price: The price of the depth.
        amount: The amount of the depth.
    """

    def __init__(self):
        self.price = 0.0
        self.amount = 0.0

    @staticmethod
    def json_parse(data_array):
        entry = DepthEntry()
        entry.price = data_array[0]
        entry.amount = data_array[1]
        return entry

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.amount, format_data + "Amount")