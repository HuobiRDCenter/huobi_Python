from huobi.model.accountsupdate import AccountsUpdate



class AccountsUpdateEvent:
    """
    subscribe for account balance change.

    :member
        action: here only support sub
        ch: subscribe topic, such as "accounts.update#0"
        data: return data, type is AccountsUpdate
    """
    def __init__(self):
        self.action = ""
        self.ch = 0
        self.seq = 0
        self.data = AccountsUpdate()

    @staticmethod
    def json_parse(json_wrapper):
        upd_event = AccountsUpdateEvent()
        upd_event.ch = json_wrapper.get_string("ch")
        upd_event.action = json_wrapper.get_string("action")
        upd_event.seq = json_wrapper.get_int_or_default("seq", 0)
        upd_event.data = AccountsUpdate.json_parse(json_wrapper.get_object_or_default("data", {}))
        return upd_event


    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        self.data.print_object()