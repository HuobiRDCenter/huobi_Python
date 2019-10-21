class BatchCancelResult:
    """
    The result of batch cancel operation.

    :member
        success_count: The number of cancel request sent successfully.
        failed_count: The number of cancel request failed.

    """

    def __init__(self):
        self.success_count = 0
        self.failed_count = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.success_count, format_data + "Success Count")
        PrintBasic.print_basic(self.failed_count, format_data + "Failed Count")