from huobi.constant import *


class OrderUpdate:
    """
    The detail order information.

    :member
        orderId: The order id.
        tradePrice: trade price
        tradeVolume: trade volume
        tradeId: Id record for trade
        tradeTime: trade timestamp (ms)
        aggressor: true (taker), false (maker)
        remainAmt: Remaining amount (for buy-market order it's remaining value)
        orderStatus: Order status, valid value: partial-filled, filled
        clientOrderId: Client order ID (if any)
        eventType: Event type, valid value: trade
        symbol: The symbol, like "btcusdt".
        type: The order type, possible values are: buy-market, sell-market, buy-limit, sell-limit, buy-ioc, sell-ioc, buy-limit-maker, sell-limit-maker, buy-limit-fok, sell-limit-fok.
    """

    def __init__(self):
        self.orderId = 0
        self.tradePrice = ""
        self.tradeVolume = ""
        self.tradeId = 0
        self.tradeTime = 0
        self.aggressor = False
        self.remainAmt = ""
        self.orderStatus = OrderState.INVALID
        self.clientOrderId = ""
        self.eventType = ""
        self.symbol = ""
        self.type = OrderType.INVALID
        self.accountId = 0
        self.orderSide = ""
        self.errCode = 0
        self.errMessage = ""
        self.lastActTime = 0
        self.orderSource = ""
        self.orderPrice = ""
        self.orderSize = ""
        self.orderValue = ""
        self.execAmt = ""



    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.orderId, format_data + "Order Id")
        PrintBasic.print_basic(self.tradePrice, format_data + "Trade Price")
        PrintBasic.print_basic(self.tradeVolume, format_data + "Trade Volume")
        PrintBasic.print_basic(self.tradeId, format_data + "Trade Id")
        PrintBasic.print_basic(self.tradeTime, format_data + "Trade Timestamp")
        PrintBasic.print_basic(self.aggressor, format_data + "is Taker")
        PrintBasic.print_basic(self.orderStatus, format_data + "Order State")
        PrintBasic.print_basic(self.clientOrderId, format_data + "Client Order Id")
        PrintBasic.print_basic(self.eventType, format_data + "Event Type")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.type, format_data + "Order Type")
        PrintBasic.print_basic(self.accountId, format_data + "Account Id")
        PrintBasic.print_basic(self.orderSide, format_data + "Order Side")
        PrintBasic.print_basic(self.errCode, format_data + "Error Code")
        PrintBasic.print_basic(self.errMessage, format_data + "Error Message")
        PrintBasic.print_basic(self.lastActTime, format_data + "Last Actual Time")
        PrintBasic.print_basic(self.orderSource, format_data + "Order Source")
        PrintBasic.print_basic(self.orderPrice, format_data + "Order Price")
        PrintBasic.print_basic(self.orderSize, format_data + "Order Size")
        PrintBasic.print_basic(self.orderValue, format_data + "Order Value")
        PrintBasic.print_basic(self.execAmt, format_data + "Exec Amount")




