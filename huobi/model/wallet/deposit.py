from huobi.constant import *


class Deposit:
    """
    The latest status for deposits

    :member
        id: The transfer id.
        currency: The crypto currency to deposit.
        tx_hash: The on-chain transaction hash.
        amount: The number of crypto asset transferred in its minimum unit.
        address: The deposit source address.
        address_tag: The user defined address tag.
        fee: The amount of fee taken by Huobi in this crypto's minimum unit.
        created_at: The UNIX formatted timestamp in UTC for the transfer creation.
        updated_at: The UNIX formatted timestamp in UTC for the transfer's latest update.
        state: The deposit state of this transfer.
    """

    def __init__(self):
        self.id = 0
        self.type = DepositWithdraw.DEPOSIT
        self.currency = ""
        self.tx_hash = ""
        self.amount = 0.0
        self.chain = ""
        self.address = ""
        self.address_tag = ""
        self.fee = 0.0
        self.created_at = 0
        self.updated_at = 0
        self.state = DepositState.INVALID

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.type, format_data + "Operate Type")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.chain, format_data + "Chain")
        PrintBasic.print_basic(self.tx_hash, format_data + "Trade Hash")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.address, format_data + "Address")
        PrintBasic.print_basic(self.address_tag, format_data + "Address Tag")
        PrintBasic.print_basic(self.fee, format_data + "Fee")
        PrintBasic.print_basic(self.state, format_data + "Deposit State")
        PrintBasic.print_basic(self.created_at, format_data + "Create Time")
        PrintBasic.print_basic(self.updated_at, format_data + "Update Time")
