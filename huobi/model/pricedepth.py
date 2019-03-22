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
