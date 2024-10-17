class Failed:

    def __init__(self):
        self.order_id = ""
        self.client_order_id = ""
        self.err_code = ""
        self.err_msg = ""
        self.order_state = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.order_id, format_data + "Symbol")
        PrintBasic.print_basic(self.client_order_id, format_data + "Maker Fee")
        PrintBasic.print_basic(self.err_code, format_data + "Taker Fee")
        PrintBasic.print_basic(self.err_msg, format_data + "Error Massage")
        PrintBasic.print_basic(self.order_state, format_data + "Order State")
