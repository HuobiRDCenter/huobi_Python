
from huobi.utils.input_checker import *


class MarginClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """
        self.__kwargs = kwargs

    def post_transfer_in_margin(self, symbol: 'str', currency: 'str', amount: 'float') -> int:
        """
        Transfer asset from spot account to margin account.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param currency: The currency of transfer. (mandatory)
        :param amount: The amount of transfer. (mandatory)
        :return:
        """
        check_symbol(symbol)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "symbol": symbol,
            "currency": currency,
            "amount": amount
        }

        from huobi.service.margin.post_transfer_in_margin import PostTransferInMarginService
        return PostTransferInMarginService(params).request(**self.__kwargs)

    def post_transfer_out_margin(self, symbol: 'str', currency: 'str', amount: 'float') -> int:
        """
        Transfer asset from margin account to spot account.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param currency: The currency of transfer. (mandatory)
        :param amount: The amount of transfer. (mandatory)
        :return:
        """
        check_symbol(symbol)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "symbol": symbol,
            "currency": currency,
            "amount": amount
        }

        from huobi.service.margin.post_transfer_out_margin import PostTransferOutMarginService
        return PostTransferOutMarginService(params).request(**self.__kwargs)

    def get_margin_account_balance(self, symbol: 'str') -> list:
        """
        Get the Balance of the Margin Loan Account.

        :param symbol: The currency, like "btc". (mandatory)
        :return: The margin loan account detail list.
        """
        check_symbol(symbol)

        params = {
            "symbol": symbol
        }

        from huobi.service.margin.get_margin_account_balance import GetMarginAccountBalanceService
        return GetMarginAccountBalanceService(params).request(**self.__kwargs)

    def post_create_margin_order(self, symbol: 'str', currency: 'str', amount: 'float') -> int:
        """
        Submit a request to borrow with margin account.

        :param symbol: The trading symbol to borrow margin, e.g. "btcusdt", "bccbtc". (mandatory)
        :param currency: The currency to borrow,like "btc". (mandatory)
        :param amount: The amount of currency to borrow. (mandatory)
        :return: The margin order id.
        """
        check_symbol(symbol)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "symbol": symbol,
            "currency" : currency,
            "amount" : amount
        }

        from huobi.service.margin.post_create_margin_order import PostCreateMarginOrderService
        return PostCreateMarginOrderService(params).request(**self.__kwargs)

    def post_repay_margin_order(self, load_id: 'int', amount: 'float') -> int:
        """
        Get the margin loan records.

        :param load_id: The previously returned order id when loan order was created. (mandatory)
        :param amount: The amount of currency to repay. (mandatory)
        :return: The margin order id.
        """
        check_should_not_none(load_id, "load_id")
        check_should_not_none(amount, "amount")

        params = {
            "load_id": load_id,
            "amount": amount
        }

        from huobi.service.margin.post_repay_margin_order import PostRepayMarginOrderService
        return PostRepayMarginOrderService(params).request(**self.__kwargs)

    def get_margin_loan_orders(self, symbol: 'str', start_date: 'str' = None, end_date: 'str' = None,
                         states: 'LoanOrderState' = None, from_id: 'int' = None,
                         size: 'int' = None, direction: 'QueryDirection' = None) -> list:
        """
        Get the margin loan records.

        :param symbol: The symbol, like "btcusdt" (mandatory).
        :param start_date: The search starts date in format yyyy-mm-dd. (optional).
        :param end_date: The search end date in format yyyy-mm-dd.(optional, can be null).
        :param states: The loan order states, it could be created, accrual, cleared or invalid. (optional)
        :param from_id: Search order id to begin with. (optional)
        :param size: The number of orders to return.. (optional)
        :param direction: The query direction, prev or next. (optional)
        :return: The list of the margin loan records.
        """

        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")

        params = {
            "symbol" : symbol,
            "start-date" : start_date,
            "end-date" : end_date,
            "states" : states,
            "from" : from_id,
            "size" : size,
            "direct" : direction
        }

        from huobi.service.margin.get_margin_loan_orders import GetMarginLoanOrdersService
        return GetMarginLoanOrdersService(params).request(**self.__kwargs)
