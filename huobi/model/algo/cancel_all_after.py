class CancelAllAfter:

    def __init__(self):
        self.currentTime = 0
        self.triggerTime = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currentTime, format_data + "currentTime")
        PrintBasic.print_basic(self.triggerTime, format_data + "triggerTime")

