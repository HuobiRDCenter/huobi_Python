

class PriceDepthSerial:

    @staticmethod
    def get_depth_step_list():
        return [DepthStep.STEP0,
                DepthStep.STEP1,
                DepthStep.STEP2,
                DepthStep.STEP3,
                DepthStep.STEP4,
                DepthStep.STEP5]

    @staticmethod
    def get_valid_depth_step(value, defalut_value):
        step_list = PriceDepth.get_depth_step_list()
        if value in step_list:
            return value
        else:
            return defalut_value

    @staticmethod
    def json_parse(json_data):
        price_depth = PriceDepth()
        price_depth.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        bid_list = list()
        bids_array = json_data.get_array("bids")
        for item in bids_array.get_items_as_array():
            depth_entry = DepthEntry()
            depth_entry.price = item.get_float_at(0)
            depth_entry.amount = item.get_float_at(1)
            bid_list.append(depth_entry)
        ask_list = list()
        asks_array = json_data.get_array("asks")
        for item in asks_array.get_items_as_array():
            depth_entry = DepthEntry()
            depth_entry.price = item.get_float_at(0)
            depth_entry.amount = item.get_float_at(1)
            ask_list.append(depth_entry)
        price_depth.bids = bid_list
        price_depth.asks = ask_list

        return price_depth

