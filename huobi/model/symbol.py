class Symbol:
    """
    The Huobi supported symbols.

    :member
        base_currency: The base currency in a trading symbol.
        quote_currency: The quote currency in a trading symbol.
        price_precision: The quote currency precision when quote price (decimal places).
        amount_precision: The base currency precision when quote amount (decimal places).
        symbol_partition: The trading section, possible values: [main，innovation，bifurcation].
        symbol: The symbol, like "btcusdt".
        state : trade status, maybe one in [online，offline,suspend]
        value_precision : value precision
        min_order_amt : minimum volume limit only used in limit-order and sell-market order
        max_order_amt : Maximum volume
        min_order_value : Minimum order amount
        leverage_ratio : Leverage ratio for symbol
    """

    def __init__(self):
        self.base_currency = ""
        self.quote_currency = ""
        self.price_precision = 0
        self.amount_precision = 0
        self.symbol_partition = ""
        self.symbol = ""
        self.state = ""
        self.value_precision = 0
        self.min_order_amt = ""
        self.max_order_amt = ""
        self.min_order_value = ""
        self.leverage_ratio = 0
