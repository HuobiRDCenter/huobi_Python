class OrderHistoryItem:
    """
    The result of batch cancel operation.

    :member
        orderOrigTime
        lastActTime
        symbol
        source
        orderSide
        orderType
        timeInForce
        clientOrderId
        accountId
        orderPrice
        orderSize
        stopPrice
        orderStatus

    """

    def __init__(self):
        self.orderOrigTime = ""
        self.lastActTime = ""
        self.symbol = ""
        self.source = ""
        self.orderSide = ""
        self.orderType = ""
        self.timeInForce = ""
        self.clientOrderId = ""
        self.accountId = ""
        self.orderPrice = ""
        self.orderSize = ""
        self.stopPrice = ""
        self.orderStatus = ""
        self.orderId = ""
        self.orderValue = ""
        self.trailingRate = ""
        self.orderCreateTime = ""
        self.errCode = ""
        self.errMessage = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.orderOrigTime, format_data + "")
        PrintBasic.print_basic(self.lastActTime, format_data + "")
        PrintBasic.print_basic(self.symbol, format_data + "")
        PrintBasic.print_basic(self.source, format_data + "")
        PrintBasic.print_basic(self.orderSide, format_data + "")
        PrintBasic.print_basic(self.orderType, format_data + "")
        PrintBasic.print_basic(self.timeInForce, format_data + "")
        PrintBasic.print_basic(self.clientOrderId, format_data + "")
        PrintBasic.print_basic(self.accountId, format_data + "")
        PrintBasic.print_basic(self.orderPrice, format_data + "")
        PrintBasic.print_basic(self.orderSize, format_data + "")
        PrintBasic.print_basic(self.stopPrice, format_data + "")
        PrintBasic.print_basic(self.orderStatus, format_data + "")
        PrintBasic.print_basic(self.orderId, format_data + "")
        PrintBasic.print_basic(self.orderValue, format_data + "")
        PrintBasic.print_basic(self.trailingRate, format_data + "")
        PrintBasic.print_basic(self.orderCreateTime, format_data + "")
        PrintBasic.print_basic(self.errCode, format_data + "")
        PrintBasic.print_basic(self.errMessage, format_data + "")
