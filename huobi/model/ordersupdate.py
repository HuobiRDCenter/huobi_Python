from huobi.model import OrderType, OrderState, OrderUpdateEventType


class OrdersUpdate:

    def __init__(self):
        self.eventType = OrderUpdateEventType.INVALID
        self.symbol = ""
        self.orderId = 0
        self.clientOrderId = ""
        self.type = OrderType.INVALID
        self.orderStatus = OrderState.INVALID
        self.orderPrice = ""
        self.orderSize = ""
        self.orderCreateTime = 0
        self.tradeId = 0
        self.tradePrice = ""
        self.tradeVolume = ""
        self.tradeTime = 0
        self.aggressor = False
        self.remainAmt = ""
        self.lastActTime = 0

    @staticmethod
    def json_parse(json_data):
        obj = OrdersUpdate()
        obj.eventType = json_data.get_string("eventType")
        obj.symbol = json_data.get_string("symbol")
        obj.orderId = json_data.get_int("orderId")
        obj.clientOrderId = json_data.get_string("clientOrderId")
        obj.orderStatus = json_data.get_string("orderStatus")

        if obj.eventType == OrderUpdateEventType.CREATION:
            obj.type = json_data.get_string_or_default("type", OrderType.INVALID)
            obj.orderPrice = json_data.get_string_or_default("orderPrice", "")
            obj.orderSize = json_data.get_string_or_default("orderSize", "")
            obj.orderCreateTime = json_data.get_int_or_default("orderCreateTime", 0)

        if obj.eventType == OrderUpdateEventType.TRADE:
            obj.tradeId = json_data.get_int_or_default("tradeId", 0)
            obj.tradePrice = json_data.get_string_or_default("tradePrice", "")
            obj.tradeVolume = json_data.get_string_or_default("tradeVolume", "")
            obj.tradeTime = json_data.get_int_or_default("tradeTime", 0)
            obj.aggressor = json_data.get_boolean("aggressor", False)
            obj.remainAmt = json_data.get_string_or_default("remainAmt", "")

        if obj.eventType == OrderUpdateEventType.TRADE:
            obj.lastActTime = json_data.get_int_or_default("lastActTime", 0)

        return obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.eventType, format_data + "Event Type")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.orderId, format_data + "Order Id")
        PrintBasic.print_basic(self.clientOrderId, format_data + "Client Order Id")
        PrintBasic.print_basic(self.orderStatus, format_data + "order Status")

        if self.eventType == OrderUpdateEventType.CREATION:
            PrintBasic.print_basic(self.type, format_data + "Type")
            PrintBasic.print_basic(self.orderPrice, format_data + "order Price")
            PrintBasic.print_basic(self.orderSize, format_data + "order Size")
            PrintBasic.print_basic(self.orderCreateTime, format_data + "Order Create Time")

        if self.eventType == OrderUpdateEventType.TRADE:
            PrintBasic.print_basic(self.tradeId, format_data + "Trade Id")
            PrintBasic.print_basic(self.tradePrice, format_data + "Trade Price")
            PrintBasic.print_basic(self.tradeVolume, format_data + "Trade Volume")
            PrintBasic.print_basic(self.tradeTime, format_data + "Trade Time")
            PrintBasic.print_basic(self.aggressor, format_data + "is aggressor")
            PrintBasic.print_basic(self.remainAmt, format_data + "Remain Amount")

        if self.eventType == OrderUpdateEventType.CANCELLATION:
            PrintBasic.print_basic(self.lastActTime, format_data + "Last Activity Time")
