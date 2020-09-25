class OrderListItem:
    """
    The result of batch cancel operation.

    :member
        event_type:
        symbol:
        order_id:
        trade_price:
        trade_volume:
        order_side:
        aggressor:
        trade_id:
        trade_time:
        transact_fee:
        fee_deduct:
        fee_deduct_type:
        fee_currency:
        account_id:
        source:
        order_price:
        order_size:
        client_order_id:
        order_create_time:
        order_status:
    """

    def __init__(self):
        self.eventType = ""
        self.symbol = ""
        self.orderId = ""
        self.tradePrice = ""
        self.tradeVolume = ""
        self.orderSide = ""
        self.aggressor = ""
        self.tradeId = ""
        self.tradeTime = ""
        self.transactFee = ""
        self.feeDeduct = ""
        self.feeDeductType = ""
        self.feeCurrency = ""
        self.accountId = ""
        self.source = ""
        self.orderPrice = ""
        self.orderSize = ""
        self.clientOrderId = ""
        self.orderCreateTime = ""
        self.orderStatus = ""
        self.trailingRate = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.eventType, format_data + "Event Type")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.orderId, format_data + "OrderId")
        PrintBasic.print_basic(self.tradePrice, format_data + "Trade Price")
        PrintBasic.print_basic(self.tradeVolume, format_data + "Trade Volume")
        PrintBasic.print_basic(self.orderSide, format_data + "Order Side")
        PrintBasic.print_basic(self.aggressor, format_data + "Aggressor")
        PrintBasic.print_basic(self.tradeId, format_data + "TradeId")
        PrintBasic.print_basic(self.tradeTime, format_data + "Trade Time")
        PrintBasic.print_basic(self.transactFee, format_data + "Transact Fee")
        PrintBasic.print_basic(self.feeDeduct, format_data + "Fee Deduct")
        PrintBasic.print_basic(self.feeDeductType, format_data + "Fee Deduct Type")
        PrintBasic.print_basic(self.feeCurrency, format_data + "Fee Currency")
        PrintBasic.print_basic(self.accountId, format_data + "Account Id")
        PrintBasic.print_basic(self.source, format_data + "Source")
        PrintBasic.print_basic(self.orderPrice, format_data + "Order Price")
        PrintBasic.print_basic(self.orderSize, format_data + "Order Size")
        PrintBasic.print_basic(self.clientOrderId, format_data + "Client Order Id")
        PrintBasic.print_basic(self.orderCreateTime, format_data + "Order Create Time")
        PrintBasic.print_basic(self.orderStatus, format_data + "Order Status")
        PrintBasic.print_basic(self.trailingRate, format_data + "Trailing Rate (Trailing Order Only)")
