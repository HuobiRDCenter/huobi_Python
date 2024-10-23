class ExchangeInfo:
    """
    The Huobi supported the symbols and currencies.

    :member
        symbol_list: The symbol list. The content is Symbol class.
        currencies: The currency list. The content is string value.
    """

    def __init__(self):
        self.symbol_list = list()
        self.currencies = list()
