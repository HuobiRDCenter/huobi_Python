

from huobi.model.market.depth_entry import DepthEntry

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
        mbp.seqNum = json_data.get("seqNum", 0)
        mbp.prevSeqNum = json_data.get("prevSeqNum", 0)  # prevSeqNum only for increased subscribe, request doesn't have this value
        for item in json_data.get("bids", []):
            depth_entry = DepthEntry()
            depth_entry.price = item[0]
            depth_entry.amount = item[1]
            bid_list.append(depth_entry)
        ask_list = list()
        for item in json_data.get("asks", []):
            depth_entry = DepthEntry()
            depth_entry.price = item[0]
            depth_entry.amount = item[1]
            ask_list.append(depth_entry)
        mbp.bids = bid_list
        mbp.asks = ask_list

        return mbp



    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.seqNum, format_data + "seqNum")
        PrintBasic.print_basic(self.prevSeqNum, format_data + "prevSeqNum")
        for entry in self.bids:
            PrintBasic.print_basic(str(entry.price) + ", amount: " + str(entry.amount), format_data + "Bids price: ")

        for entry in self.asks:
            PrintBasic.print_basic(str(entry.price) + ", amount: " + str(entry.amount), format_data + "Asks price: ")
