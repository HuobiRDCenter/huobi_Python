class SubuserApikeyGeneration:
    """
    The trade information with price and amount etc.

    :member
        accessKey:
        secretKey:
        note:
        permission: "trade,readOnly",
        ipAddresses":
    """

    def __init__(self):
        self.accessKey = ""
        self.secretKey = ""
        self.note = ""
        self.permission = ""
        self.ipAddresses = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accessKey, format_data + "accessKey")
        PrintBasic.print_basic(self.secretKey, format_data + "secretKey")
        PrintBasic.print_basic(self.note, format_data + "note")
        PrintBasic.print_basic(self.permission, format_data + "permission")
        PrintBasic.print_basic(self.ipAddresses, format_data + "ipAddresses")
