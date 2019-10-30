
class ChainDepositAddress:
    """
    The deposit address.

    :member
        currency: The crypto currency to deposit.
        address: Deposit address
        addressTag: Deposit address tag.
        chain: Block chain name.
    """
    def __init__(self):
        self.currency = ""
        self.address = ""
        self.addressTag = ""
        self.chain = ""



    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.address, format_data + "Address")
        PrintBasic.print_basic(self.addressTag, format_data + "addressTag")
        PrintBasic.print_basic(self.chain, format_data + "Chain")

