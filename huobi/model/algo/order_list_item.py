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
        self.accountId = ""
        self.source = ""
        self.clientOrderId = ""
        self.symbol = ""
        self.orderPrice = ""
        self.orderSize = ""
        self.orderValue = ""
        self.orderSide = ""
        self.timeInForce = ""
        self.orderType = ""
        self.stopPrice = ""
        self.trailingRate = ""
        self.orderOrigTime = ""
        self.lastActTime = ""
        self.orderStatus = ""


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accountId, format_data + "Account Id")
        PrintBasic.print_basic(self.source, format_data + "Source")
        PrintBasic.print_basic(self.clientOrderId, format_data + "Client Order Id")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.orderPrice, format_data + "Order Price")
        PrintBasic.print_basic(self.orderSize, format_data + "Order Size")
        PrintBasic.print_basic(self.orderValue, format_data + "Order Value")
        PrintBasic.print_basic(self.orderSide, format_data + "Order Side")
        PrintBasic.print_basic(self.timeInForce, format_data + "Time In Force")
        PrintBasic.print_basic(self.orderType, format_data + "Order Type")
        PrintBasic.print_basic(self.stopPrice, format_data + "Stop Price")
        PrintBasic.print_basic(self.trailingRate, format_data + "Trailing Rate")
        PrintBasic.print_basic(self.orderOrigTime, format_data + "Order Origin Time")
        PrintBasic.print_basic(self.lastActTime, format_data + "Last Actual Time")
        PrintBasic.print_basic(self.orderStatus, format_data + "Order Status")