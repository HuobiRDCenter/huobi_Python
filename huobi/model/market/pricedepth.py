
class PriceDepth:
    """
    The price depth information.

    :member
        ts: The UNIX formatted timestamp in UTC.
        version:
        bids: The list of the bid depth. The content is DepthEntry class.
        asks: The list of the ask depth. The content is DepthEntry class.

    """
    def __init__(self):
        self.ts = 0
        self.version = 0
        self.bids = list()
        self.asks = list()



    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ts, format_data + "UTC Time")
        PrintBasic.print_basic(self.version, format_data + "Version")
        if len(self.bids):
            i = 0
            print(format_data, "---- Top " + str(len(self.bids)) + " bids ----")
            for entry in self.bids:
                i = i + 1
                print(format_data, str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))
                #print()

        if len(self.asks):
            i = 0
            print(format_data, "---- Top " + str(len(self.asks)) + " asks ----")
            for entry in self.asks:
                i = i + 1
                print(format_data, str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))
                #print()