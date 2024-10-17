class BatchCreateOrder:
    """
    batch create order result

    :member
        order_id: The transfer id.
        client_order_id: The crypto currency to deposit.
        err_code: The on-chain transaction hash.
        err_msg: The number of crypto asset transferred in its minimum unit.

    """
    def __init__(self):
        self.order_id = 0
        self.client_order_id = ""
        self.err_code = ""
        self.err_msg = ""

    def print_object(self, format_data=""):
        from huobi.utils import PrintBasic
        PrintBasic.print_basic(self.order_id, format_data + "Order Id")
        PrintBasic.print_basic(self.client_order_id, format_data + "Client Order Id")
        PrintBasic.print_basic(self.err_code, format_data + "Error Code")
        PrintBasic.print_basic(self.err_msg, format_data + "Error Message")