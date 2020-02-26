class BatchCancelFailed:
    """
    batch create order result

    :member
        order_id: The transfer id.
        client_order_id: The crypto currency to deposit.
        err_code: The on-chain transaction hash.
        err_msg: The number of crypto asset transferred in its minimum unit.

    """
    def __init__(self):
        self.order_id = ""
        self.client_order_id = ""
        self.err_code = ""
        self.err_msg = ""
        self.order_state = 0

    @staticmethod
    def json_parse(json_wrapper):
        fail_obj = BatchCancelFailed()
        fail_obj.order_id = json_wrapper.get_string_or_default("order-id", "")
        fail_obj.client_order_id = json_wrapper.get_string_or_default("client-order-id", "")
        fail_obj.err_code = json_wrapper.get_string_or_default("err-code", "")
        fail_obj.err_msg = json_wrapper.get_string_or_default("err-msg", "")
        fail_obj.order_state = json_wrapper.get_string_or_default("order-state", "")
        return fail_obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.order_id, format_data + "Order Id")
        PrintBasic.print_basic(self.client_order_id, format_data + "Client Order Id")
        PrintBasic.print_basic(self.err_code, format_data + "Error Code")
        PrintBasic.print_basic(self.err_msg, format_data + "Error Msg")
        PrintBasic.print_basic(self.order_state, format_data + "Order State")


class BatchCancelOrder:
    """
    The result of batch cancel result, it will list .

    :member
        success: success order id list.
        failed: failed order id list.

    """
    def __init__(self):
        self.success = list()
        self.failed = list()

    @staticmethod
    def json_parse(json_wrapper):
        obj = BatchCancelOrder()
        data_object = json_wrapper.get_object("data")
        success_array = data_object.get_array("success")
        failed_array = data_object.get_array("failed")

        obj.success = success_array.get_items_as_string()

        for item in failed_array.get_items():
            obj.failed.append(BatchCancelFailed.json_parse(item))

        return obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintList
        print("Success Order Id List")
        PrintList.print_object_list(self.success)
        print()

        print("Failed Order Id List")
        if len(self.failed):
            for item in self.failed:
                item.print_object(format_data)
                print()

