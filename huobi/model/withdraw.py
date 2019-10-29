from huobi.model.constant import *


class Withdraw:
    """
    The latest status for withdraws.

    :member
        id: The transfer id.
        currency: The crypto currency to deposit.
        tx_hash: The on-chain transaction hash.
        amount: The number of crypto asset transferred in its minimum unit.
        address: The deposit source address.
        address_tag: The user defined address tag.
        fee: The amount of fee taken by Huobi in this crypto's minimum unit.
        created_timestamp: The UNIX formatted timestamp in UTC for the transfer creation.
        updated_timestamp: The UNIX formatted timestamp in UTC for the transfer's latest update.
        withdraw_state: The withdraw state of this transfer.
    """
    def __init__(self):
        self.id = 0
        self.currency = ""
        self.tx_hash = ""
        self.amount = 0.0
        self.type = ""
        self.chain = ""
        self.address = ""
        self.address_tag = ""
        self.fee = 0.0
        self.created_timestamp = 0
        self.updated_timestamp = 0
        self.withdraw_state = WithdrawState.INVALID

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.type, format_data + "Operator Type")
        PrintBasic.print_basic(self.chain, format_data + "Chain")
        PrintBasic.print_basic(self.tx_hash, format_data + "Trade Hash")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.address, format_data + "Address")
        PrintBasic.print_basic(self.address_tag, format_data + "Address Tag")
        PrintBasic.print_basic(self.fee, format_data + "Fee")
        PrintBasic.print_basic(self.withdraw_state, format_data + "Withdraw State")
        PrintBasic.print_basic(self.created_timestamp, format_data + "Create Time")
        PrintBasic.print_basic(self.updated_timestamp, format_data + "Update Time")