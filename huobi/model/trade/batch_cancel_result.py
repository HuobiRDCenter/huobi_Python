class BatchCancelResult:
    """
    The result of batch cancel operation.

    :member
        success_count: The number of cancel request sent successfully.
        failed_count: The number of cancel request failed.

    """

    def __init__(self):
        self.success = []
        self.failed = []

    def print_object(self, format_data=""):
        print("Success Order Counts", len(self.success), " Success Order Ids : ", self.success)
        print("Fail Order Counts", len(self.failed), " Fail Order Ids : ", self.failed)