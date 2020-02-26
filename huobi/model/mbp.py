from huobi.model.constant import DepthStep
from huobi.model.depthentry import DepthEntry


class Mbp:
    """
    Increasement of price depth information.

    :member
        seqNum: current seqNum.
        prevSeqNum: previous seqNum.
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.seqNum = 0
        self.prevSeqNum = 0
        self.bids = list()
        self.asks = list()

    @staticmethod
    def json_parse(json_data):
        mbp = Mbp()
        bid_list = list()
        mbp.seqNum = json_data.get_int("seqNum")
        mbp.prevSeqNum = json_data.get_int_or_default("prevSeqNum", 0)  # prevSeqNum only for increased subscribe, request doesn't have this value
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
        mbp.bids = bid_list
        mbp.asks = ask_list

        return mbp
