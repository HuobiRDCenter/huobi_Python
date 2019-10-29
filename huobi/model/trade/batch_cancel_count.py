


class BatchCancelCount:
    """
    The result of batch cancel operation.

    :member
        success_count: The number of cancel request sent successfully.
        failed_count: The number of cancel request failed.
        next_id:next open order id
    """

    def __init__(self):
        self.success_count = 0
        self.failed_count = 0
        self.next_id = -1

    def print_object(self, format_data=""):
        from huobi.utils import PrintBasic
        PrintBasic.print_basic(self.success_count, format_data + "Success Count")
        PrintBasic.print_basic(self.failed_count, format_data + "Failed Count")
        PrintBasic.print_basic(self.next_id, format_data + "Next Open Order ID")