from huobi.model.constant import *


class TradeClearing:
    """
    The detail order information.

    :member
        order_id: The order id.
        symbol: The symbol, like "btcusdt".
        tradePrice: trade price.
        tradeVolume: trade Volume.
        orderSide: order Side, more to see OrderSide
        orderType: order type, more to see OrderType
        aggressor: is aggressor, only true or false
        tradeId: trade ID.
        tradeTime: trade Time.
        transactFee: transact Fee.
        feeDeduct: Deduct Fee.
        feeDeductType: fee Deduct Type, current only support ht and point
    """

    def __init__(self):
        self.symbol = ""
        self.orderId = 0
        self.tradePrice = ""
        self.tradeVolume = ""
        self.orderSide = OrderSide.INVALID
        self.orderType = OrderType.INVALID
        self.aggressor = False
        self.tradeId = 0
        self.tradeTime = 0
        self.transactFee = ""
        self.feeDeduct = ""
        self.feeDeductType = FeeDeductType.INVALID

    @staticmethod
    def json_parse(json_data):
        obj = TradeClearing()
        if json_data and json_data.contain_key("orderId"):
            obj.symbol = json_data.get_string("symbol")
            obj.orderId = json_data.get_int("orderId")
            obj.tradePrice = json_data.get_string("tradePrice")
            obj.tradeVolume = json_data.get_string("tradeVolume")
            obj.orderSide = json_data.get_string("orderSide")
            obj.orderType = json_data.get_string("orderType")
            obj.aggressor = json_data.get_boolean("aggressor")
            obj.tradeId = json_data.get_int("tradeId")
            obj.tradeTime = json_data.get_int("tradeTime")
            obj.transactFee = json_data.get_string("transactFee")
            obj.feeDeduct = json_data.get_string("feeDeduct")
            obj.feeDeductType = json_data.get_string("feeDeductType")

        return obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.orderId, format_data + "Order Id")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.tradePrice, format_data + "Trade Price")
        PrintBasic.print_basic(self.tradeVolume, format_data + "Trade Volume")
        PrintBasic.print_basic(self.orderSide, format_data + "Order Side")
        PrintBasic.print_basic(self.orderType, format_data + "Order Type")
        PrintBasic.print_basic(self.aggressor, format_data + "is aggressor")
        PrintBasic.print_basic(self.tradeId, format_data + "Trade Id")
        PrintBasic.print_basic(self.tradeTime, format_data + "Trade Time")
        PrintBasic.print_basic(self.transactFee, format_data + "Transact Fee")
        PrintBasic.print_basic(self.feeDeduct, format_data + "Fee Deduct")
        PrintBasic.print_basic(self.feeDeductType, format_data + "Fee Deduct Type")


