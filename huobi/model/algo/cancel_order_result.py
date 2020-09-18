class CancelOrderResult:
    """
    The result of batch cancel operation.

    :member
        accepted: The clientOrderIds accepted.
        rejected: The clientOrderIds rejected .

    """

    def __init__(self):
        self.accepted = []
        self.rejected = []

    def print_object(self, format_data=""):
        print("Success Order Counts", len(self.accepted), " accepted Order Ids : ", self.accepted)
        print("Fail Order Counts", len(self.rejected), " Rejected Order Ids : ", self.rejected)