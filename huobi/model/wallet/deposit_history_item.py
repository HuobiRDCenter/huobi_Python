from huobi.constant import *


class DepositHistoryItem:
    """
     The deposit history

     :member
         id: The transfer id.
         currency: The crypto currency to deposit.
         txHash: The on-chain transaction hash.
         amount: The number of crypto asset transferred in its minimum unit.
         address: The deposit source address.
         addressTag: The user defined address tag.
         deposit_state: The deposit state of this transfer.
         created_timestamp: The UNIX formatted timestamp in UTC for the transfer creation.
         updated_timestamp: The UNIX formatted timestamp in UTC for the transfer's latest update.
     """
    def __init__(self):
        self.id = 0
        self.currency = ""
        self.txHash = ""
        self.chain = ""
        self.amount = 0.0
        self.address = ""
        self.addressTag = ""
        self.deposit_state = WithdrawState.INVALID
        self.created_timestamp = 0
        self.updated_timestamp = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.chain, format_data + "Chain")
        PrintBasic.print_basic(self.txHash, format_data + "Trade Hash")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.address, format_data + "Address")
        PrintBasic.print_basic(self.addressTag, format_data + "Address Tag")
        PrintBasic.print_basic(self.deposit_state, format_data + "Deposit State")
        PrintBasic.print_basic(self.created_timestamp, format_data + "Create Time")
        PrintBasic.print_basic(self.updated_timestamp, format_data + "Update Time")
