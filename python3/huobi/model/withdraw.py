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
        self.address = ""
        self.address_tag = ""
        self.fee = 0.0
        self.created_timestamp = 0
        self.updated_timestamp = 0
        self.withdraw_state = WithdrawState.INVALID
