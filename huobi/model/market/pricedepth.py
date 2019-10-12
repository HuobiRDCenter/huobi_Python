
class PriceDepth:
    """
    The price depth information.

    :member
        timestamp: The UNIX formatted timestamp in UTC.
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.timestamp = 0
        self.bids = list()
        self.asks = list()



    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.timestamp, format_data + "Timestamp")
        if len(self.bids):
            print("---- Top " + str(len(self.bids)) + " bids ----")
            for entry in self.bids:
                i = i + 1
                print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))
                print()

        if len(self.asks):
            print("---- Top " + str(len(self.asks)) + " asks ----")
            for entry in self.asks:
                i = i + 1
                print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))
                print()