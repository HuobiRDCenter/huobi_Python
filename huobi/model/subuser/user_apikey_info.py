class UserApikeyInfo:
    """
    The trade information with price and amount etc.

    :member
        accessKey: .
        createTime:
        ipAddresses: .
        note:
        permission:
        status:
        updateTime:
        validDays:

    """

    def __init__(self):
        self.accessKey = ""
        self.createTime = 0
        self.ipAddresses = ""
        self.note = ""
        self.permission = ""
        self.status = ""
        self.updateTime = 0
        self.validDays = -1

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic

        PrintBasic.print_basic(self.accessKey, format_data + "accessKey")
        PrintBasic.print_basic(self.createTime, format_data + "createTime")
        PrintBasic.print_basic(self.ipAddresses, format_data + "ipAddresses")
        PrintBasic.print_basic(self.note, format_data + "note")
        PrintBasic.print_basic(self.permission, format_data + "permission")
        PrintBasic.print_basic(self.status, format_data + "status")
        PrintBasic.print_basic(self.updateTime, format_data + "updateTime")
        PrintBasic.print_basic(self.validDays, format_data + "validDays")
