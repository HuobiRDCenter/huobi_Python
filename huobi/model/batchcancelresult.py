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
