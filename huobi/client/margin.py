
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

    def post_repay_margin_order(self, loan_id: 'int', amount: 'float') -> int:
        """
        Get the margin loan records.

        :param load_id: The previously returned order id when loan order was created. (mandatory)
        :param amount: The amount of currency to repay. (mandatory)
        :return: The margin order id.
        """
        check_should_not_none(loan_id, "loan_id")
        check_should_not_none(amount, "amount")

        params = {
            "loan_id": loan_id,
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

    def get_margin_loan_info(self, symbols: 'str'=None) -> list:
        """
        The request of get margin loan info, can return currency loan info list.

        :param symbols: The symbol, like "btcusdt,htusdt". (optional)
        :return: The cross margin loan info.
        """

        check_symbol(symbols)
        params = {
            "symbols" : symbols
        }

        from huobi.service.margin.get_margin_loan_info import GetMarginLoanInfoService
        return GetMarginLoanInfoService(params).request(**self.__kwargs)

    def get_cross_margin_loan_info(self) -> list:
        """
        The request of currency loan info list.

        :return: The cross margin loan info list.
        """
        params = {}

        from huobi.service.margin.get_cross_margin_loan_info import GetCrossMarginLoanInfoService
        return GetCrossMarginLoanInfoService(params).request(**self.__kwargs)


    def post_cross_margin_transfer_in(self, currency: 'str', amount:'float') -> int:
        """
        transfer currency to cross account.

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return transfer id.
        """
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "amount": amount,
            "currency": currency
        }

        from huobi.service.margin.post_cross_margin_transfer_in import PostCrossMarginTransferInService
        return PostCrossMarginTransferInService(params).request(**self.__kwargs)

    def post_cross_margin_transfer_out(self, currency: 'str', amount:'float') -> int:
        """
        transfer currency to cross account.

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return transfer id.
        """
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "amount": amount,
            "currency": currency
        }

        from huobi.service.margin.post_cross_margin_transfer_out import PostCrossMarginTransferOutService
        return PostCrossMarginTransferOutService(params).request(**self.__kwargs)

    def post_cross_margin_create_loan_orders(self, currency:'str', amount: 'float') -> int:
        """
        create cross margin loan orders

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return order id.
        """

        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")

        params = {
            "amount": amount,
            "currency": currency
        }

        from huobi.service.margin.post_cross_margin_create_loan_orders import PostCrossMarginCreateLoanOrdersService
        return PostCrossMarginCreateLoanOrdersService(params).request(**self.__kwargs)

    def post_cross_margin_loan_order_repay(self, order_id: 'str', amount: 'float'):
        """
        repay cross margin loan orders

        :param order_id: order_id for loan (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return order id.
        """

        check_should_not_none(order_id, "order-id")
        check_should_not_none(amount, "amount")

        params = {
            "amount": amount,
            "order-id": order_id
        }

        from huobi.service.margin.post_cross_margin_loan_order_repay import PostCrossMarginLoanOrderRepayService
        return PostCrossMarginLoanOrderRepayService(params).request(**self.__kwargs)

    def get_cross_margin_loan_orders(self, currency: 'str' = None, state: 'str' = None,
                                     start_date: 'str' = None, end_date: 'str' = None,
                                     from_id: 'int' = None, size: 'int' = None, direct: 'str' = None,
                                     sub_uid: 'int' = None) -> list:
        """
        get cross margin loan orders

        :return: return list.
        """
        params = {
            "currency": currency,
            "state": state,
            "start-date": start_date,
            "end-date": end_date,
            "from": from_id,
            "size": size,
            "direct": direct,
            "sub-uid": sub_uid
        }

        from huobi.service.margin.get_cross_margin_loan_orders import GetCrossMarginLoanOrdersService
        return GetCrossMarginLoanOrdersService(params).request(**self.__kwargs)

    def get_cross_margin_account_balance(self, sub_uid:'int'=None):
        """
        get cross margin account balance

        :return: cross-margin account.
        """
        params = {
            "sub-uid": sub_uid
        }

        from huobi.service.margin.get_cross_margin_account_balance import GetCrossMarginAccountBalanceService
        return GetCrossMarginAccountBalanceService(params).request(**self.__kwargs)