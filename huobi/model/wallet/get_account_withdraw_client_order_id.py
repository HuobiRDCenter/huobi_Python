
class AccountWithdrawClientOrderId:
    def __init__(self):
        self.address = ""
        self.client_order_id = ""
        self.address_tag = ""
        self.amount = 0.0
        self.blockchain_confirm = 0
        self.chain = ""
        self.created_at = 0
        self.currency = ""
        self.error_code = ""
        self.error_msg = ""
        self.fee = 0.0
        self.from_addr_tag = ""
        self.from_address = ""
        self.id = 0
        self.request_id = ""
        self.state = ""
        self.tx_hash = ""
        self.type = ""
        self.updated_at = 0
        self.user_id = 0
        self.wallet_confirm = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.address, format_data + "address")
        PrintBasic.print_basic(self.client_order_id, format_data + "client_order_id")
        PrintBasic.print_basic(self.address_tag, format_data + "address_tag")
        PrintBasic.print_basic(self.amount, format_data + "amount")
        PrintBasic.print_basic(self.blockchain_confirm, format_data + "blockchain_confirm")
        PrintBasic.print_basic(self.chain, format_data + "chain")
        PrintBasic.print_basic(self.created_at, format_data + "created_at")
        PrintBasic.print_basic(self.currency, format_data + "currency")
        PrintBasic.print_basic(self.error_code, format_data + "error_code")
        PrintBasic.print_basic(self.error_msg, format_data + "error_msg")
        PrintBasic.print_basic(self.fee, format_data + "fee")
        PrintBasic.print_basic(self.from_addr_tag, format_data + "from_addr_tag")
        PrintBasic.print_basic(self.from_address, format_data + "from_address")
        PrintBasic.print_basic(self.id, format_data + "id")
        PrintBasic.print_basic(self.request_id, format_data + "request_id")
        PrintBasic.print_basic(self.state, format_data + "state")
        PrintBasic.print_basic(self.tx_hash, format_data + "tx_hash")
        PrintBasic.print_basic(self.type, format_data + "type")
        PrintBasic.print_basic(self.updated_at, format_data + "updated_at")
        PrintBasic.print_basic(self.user_id, format_data + "user_id")
        PrintBasic.print_basic(self.wallet_confirm, format_data + "wallet_confirm")


