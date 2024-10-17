from huobi.model.wallet.deposit_history_item import DepositHistoryItem
class DepositHistory:
    """
    The deposit history

    :member
        nextId: next id.
        data: history list.
    """

    def __init__(self):
        self.data = list()
        self.nextId = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.nextId, format_data + "NextId")
        if self.data and len(self.data):
            for item in self.data:
                item.print_object()
                PrintBasic.print_basic("", format_data + "")
