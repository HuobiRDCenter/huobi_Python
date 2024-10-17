from huobi.model.trade.failed import Failed
from huobi.utils import default_parse_list_dict


class BatchCancelResult:
    """
    The result of batch cancel operation.

    :member
        success_count: The number of cancel request sent successfully.
        failed_count: The number of cancel request failed.

    """

    def __init__(self):
        self.success = []
        self.failed = list()

    @staticmethod
    def json_parse(json_data):
        retList = []

        batch_cancel_obj = BatchCancelResult()
        batch_cancel_obj.success = json_data.get("success", "")

        failed_json = json_data.get("failed")
        result_list = default_parse_list_dict(failed_json, Failed, [])

        batch_cancel_obj.failed = result_list

        retList.append(batch_cancel_obj)

        return retList

    def print_object(self, format_data=""):
        print("Success Order Counts", len(self.success), " Success Order Ids : ", self.success)
        if self.failed and len(self.failed):
            for failed_item in self.failed:
                failed_item.print_object("\t")
                print()
