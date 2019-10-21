from huobi.model.trade import *

class BatchCancelResultSerial:

    @staticmethod
    def json_parse(json_data):
        data = json_data.get_object("data")
        batch_cancel_result = BatchCancelResult()
        batch_cancel_result.success_count = data.get_int("success-count")
        batch_cancel_result.failed_count = data.get_int("failed-count")
        return batch_cancel_result

