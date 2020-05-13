import aiohttp
import asyncio

from huobi.constant.system import RestApiDefine
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.restapiinvoker import call_sync
from huobi.impl.utils.inputchecker import *
from huobi.model import *
from huobi.impl.accountinfomap import account_info_map
from huobi.model.balance import Balance
from huobi.model.deposithistory import DepositHistory


class RequestClient(object):
    api_key = None
    server_url = None
    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        secret_key = None
        self.server_url = RestApiDefine.Url
        if "api_key" in kwargs:
            self.api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            secret_key = kwargs["secret_key"]
        if "url" in kwargs:
            self.server_url = kwargs["url"]
        try:
            self.request_impl = RestApiRequestImpl(self.api_key, secret_key, self.server_url)
            account_info_map.update_user_info(self.api_key, self.request_impl)
        except Exception:
            pass

    def get_latest_candlestick(self, symbol: 'str', interval: 'CandlestickInterval', size: 'int' = 150) -> list:
        """
        Get the latest candlestick/kline for the specified symbol.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The maximum number of candlestick/kline requested. Range [1 - 2000] (mandatory)
        :return: The list of candlestick/kline data.
        """
        return call_sync(self.request_impl.get_candlestick(symbol, interval, size, None, None))

    def get_candlestick(self, symbol: 'str', interval: 'CandlestickInterval', size: 'int' = 150,
                        start_time: 'int' = 0, end_time: 'int' = 0) -> list:
        """
        Get the candlestick/kline for the specified symbol. The data number is 150 as default.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The start time of of requested candlestick/kline data. (optional)
        :param start_time: The start time of of requested candlestick/kline data. (optional)
        :param end_time: The end time of of requested candlestick/kline data. (optional)
        :return: The list of candlestick/kline data.
        """
        return call_sync(self.request_impl.get_candlestick(symbol, interval, size, start_time, end_time))

    def get_exchange_timestamp(self) -> int:
        """
        Get the timestamp from Huobi server. The timestamp is the Unix timestamp in millisecond.
        The count shows how many milliseconds passed from Jan 1st 1970, 00:00:00.000 at UTC.
        e.g. 1546300800000 is Thu, 1st Jan 2019 00:00:00.000 UTC.

        :return: The timestamp in UTC
        """
        return call_sync(self.request_impl.get_exchange_timestamp())

    def get_price_depth(self, symbol: 'str', size: 'int' = 20) -> PriceDepth:
        """
        Get the Market Depth of a symbol.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param size: The maximum number of Market Depth requested. range [1 - 150], default is 20. (optional)
        :return: Market Depth data.
        """
        return call_sync(self.request_impl.get_price_depth(symbol, size))

    def get_last_trade(self, symbol: 'str') -> Trade:
        """
        Get the last trade with their price, volume and direction.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: The last trade with price and amount.
        """
        trade_list = call_sync(self.request_impl.get_historical_trade(symbol, None, 1))
        if trade_list is not None and len(trade_list) != 0:
            return trade_list[0]

    def get_market_trade(self, symbol: 'str') -> list:
        """
        Get the most recent trades with their price, volume and direction.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: The list of trade.
        """
        return call_sync(self.request_impl.get_market_trade(symbol))

    def get_historical_trade(self, symbol: 'str', size: 'int' = 1) -> list:
        """
        Get the most recent trades with their price, volume and direction.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param size: The number of historical trade requested, range [1 - 2000], default is 1 (optional)
        :return: The list of trade.
        """
        return call_sync(self.request_impl.get_historical_trade(symbol, None, size))

    def get_24h_trade_statistics(self, symbol: 'str') -> TradeStatistics:
        """
        Get trade statistics in 24 hours.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: Trade statistics.
        """
        return call_sync(self.request_impl.get_24h_trade_statistics(symbol))

    def get_exchange_symbol_list(self) -> list():
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument etc.

        :return: The information of trading instrument.
        """
        symbol_list = call_sync(self.request_impl.get_symbols())
        return symbol_list

    def get_exchange_currencies(self) -> list():
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading currencies.
        """
        currencies = call_sync(self.request_impl.get_currencies())
        return currencies

    def get_exchange_info(self) -> ExchangeInfo:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading instrument and currencies.
        """
        symbol_list = call_sync(self.request_impl.get_symbols())
        currencies = call_sync(self.request_impl.get_currencies())
        exchange_info = ExchangeInfo()
        exchange_info.symbol_list = symbol_list
        exchange_info.currencies = currencies
        return exchange_info

    def get_best_quote(self, symbol: 'str') -> BestQuote:
        """
        Get the best bid and ask.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: The best quote.
        """
        return call_sync(self.request_impl.get_best_quote(symbol))

    def get_withdraw_history(self, currency: 'str', from_id: 'int', size: 'int', direct=None) -> list:
        """
        Get the withdraw records of an account.

        :param currency: The currency, like "btc". (mandatory)
        :param from_id: The beginning withdraw record id. (mandatory)
        :param size: The size of record. (mandatory)
        :param direct: "prev" is order by asc, "next" is order by desc, default as "prev"
        :return: The list of withdraw records.
        """
        return call_sync(self.request_impl.get_withdraw_history(currency, from_id, size, direct))

    def get_deposit_history(self, currency: 'str', from_id: 'int', size: 'int', direct=None) -> list:
        """
        Get the deposit records of an account.

        :param currency: The currency, like "btc". (mandatory)
        :param from_id: The beginning deposit record id. (mandatory)
        :param size: The size of record. (mandatory)
        :param direct: "prev" is order by asc, "next" is order by desc, default as "prev"
        :return: The list of deposit records.
        """
        return call_sync(self.request_impl.get_deposit_history(currency, from_id, size, direct))

    def get_sub_user_deposit_history(self, sub_uid: 'int', currency: 'str' = None,
                                     start_time: 'int' = None, end_time: 'int' = None,
                                     sort: 'str' = None, limit: 'int' = None, from_id: 'int' = None) -> DepositHistory:
        """
        Parent get sub user depoist history.

        :param sub_uid: Sub user id. (mandatory)
        :param currency: Cryptocurrency.
        :param start_time: Farthest time
        :param end_time: Nearest time
        :param sort: Sorting order
        :param limit: Maximum number of items in one page
        :param from_id: First record Id in this query
        """
        return call_sync(self.request_impl.get_sub_user_deposit_history(sub_uid, currency, start_time, end_time,
                                                                        sort, limit, from_id))

    def transfer(self, symbol: 'str', from_account: 'AccountType', to_account: 'AccountType', currency: 'str',
                 amount: 'float') -> int:
        """
        Transfer asset from specified account to another account.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param from_account: The type, transfer from which account, could be SPOT or MARGIN. (mandatory)
        :param to_account: The type, transfer to which account, could be SPOT or MARGIN. (mandatory)
        :param currency: The currency of transfer. (mandatory)
        :param amount: The amount of transfer. (mandatory)
        :return:
        """
        return call_sync(self.request_impl.transfer(symbol, from_account, to_account, currency, amount))

    def apply_loan(self, symbol: 'str', currency: 'str', amount: 'float') -> int:
        """
        Submit a request to borrow with margin account.

        :param symbol: The trading symbol to borrow margin, e.g. "btcusdt", "bccbtc". (mandatory)
        :param currency: The currency to borrow,like "btc". (mandatory)
        :param amount: The amount of currency to borrow. (mandatory)
        :return: The margin order id.
        """
        return call_sync(self.request_impl.apply_loan(symbol, currency, amount))

    def repay_loan(self, load_id: 'int', amount: 'float') -> int:
        """
        Get the margin loan records.

        :param load_id: The previously returned order id when loan order was created. (mandatory)
        :param amount: The amount of currency to repay. (mandatory)
        :return: The margin order id.
        """
        return call_sync(self.request_impl.repay_loan(load_id, amount))

    def get_loan_history(self, symbol: 'str', start_date: 'str' = None, end_date: 'str' = None,
                         status: 'LoanOrderState' = None, from_id: 'int' = None,
                         size: 'int' = None, direction: 'QueryDirection' = None) -> list:
        """
        Get the margin loan records.

        :param symbol: The symbol, like "btcusdt" (mandatory).
        :param start_date: The search starts date in format yyyy-mm-dd. (optional).
        :param end_date: The search end date in format yyyy-mm-dd.(optional, can be null).
        :param status: The loan order states, it could be created, accrual, cleared or invalid. (optional)
        :param from_id: Search order id to begin with. (optional)
        :param size: The number of orders to return.. (optional)
        :param direction: The query direction, prev or next. (optional)
        :return: The list of the margin loan records.
        """
        return call_sync(self.request_impl.get_loan(symbol, start_date, end_date, status, from_id, size, direction))

    def get_last_trade_and_best_quote(self, symbol: 'str') -> LastTradeAndBestQuote:
        """
        Get last trade, best bid and best ask of a symbol.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: The data includes last trade, best bid and best ask.
        """
        best_quote = call_sync(self.request_impl.get_best_quote(symbol))
        last_trade = self.get_last_trade(symbol)
        last_trade_and_best_quote = LastTradeAndBestQuote()
        last_trade_and_best_quote.bid_amount = best_quote.bid_amount
        last_trade_and_best_quote.bid_price = best_quote.bid_price
        last_trade_and_best_quote.ask_amount = best_quote.ask_amount
        last_trade_and_best_quote.ask_price = best_quote.ask_price
        last_trade_and_best_quote.last_trade_price = last_trade.price
        last_trade_and_best_quote.last_trade_amount = last_trade.amount
        return last_trade_and_best_quote

    def get_accounts(self) -> list:
        """
        Get all accounts.

        :return: The information of all account balance.
        """
        global account_info_map
        accounts = account_info_map.get_all_accounts_without_check(self.api_key)
        if accounts and len(accounts):
            return accounts

        return call_sync(self.request_impl.get_accounts())

    async def async_get_account_balance(self, balance_full_url, account_id, ret_map):
        async with aiohttp.ClientSession() as session:
            async with session.get(balance_full_url) as resp:
                json = await resp.json()
                ret_map[account_id] = json
                return json


    def get_account_balance(self) -> list:
        """
        Get the balance of a all accounts.

        :return: The information of all account balance.
        """
        tasks = []
        accounts = self.get_accounts()
        account_balance_map = {}
        for item in accounts:
            balance_requset = self.request_impl.get_balance(item)
            balance_url = self.server_url + balance_requset.url
            tasks.append(asyncio.ensure_future(self.async_get_account_balance(balance_url, item.id, account_balance_map)))

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as ee:
            print(ee)
        finally:
            # loop.close()  #for thread safe, the event loop can't be closed
            pass

        for item in accounts:
            item.balances = Balance.parse_from_api_response(account_balance_map[ item.id])

        del account_balance_map
        del tasks
        return accounts

    def get_account_balance_by_account_type(self, account_type: "AccountType") -> Account:
        """
        Get the balance of a all accounts or specified account.

        :param account_type: The specified account type. if it is not filled, this method will return all accounts (mandatory)
        :return: The information of the account that is specified type.
        """
        check_should_not_none(account_type, "account_type")
        accounts = self.get_accounts()
        for item in accounts:
            if account_type == item.account_type:
                balances = call_sync(self.request_impl.get_balance(item))
                item.balances = balances
                return item

    def create_order(self, symbol: 'str', account_type: 'AccountType', order_type: 'OrderType', amount: 'float',
                     price: 'float', client_order_id=None, stop_price=None, operator=None) -> int:
        """
        Make an order in huobi.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_type: Account type. (mandatory)
        :param order_type: The order type. (mandatory)
        :param amount: The amount to buy (quote currency) or to sell (base currency). (mandatory)
        :param price: The limit price of limit order, only needed for limit order. (mandatory for buy-limit, sell-limit, buy-limit-maker and sell-limit-maker)
        :param client_order_id: unique Id which is user defined and must be unique in recent 24 hours
        :param stop_price: Price for auto sell to get the max benefit
        :param operator: the condition for stop_price, value can be "gte" or "lte",  gte – greater than and equal (>=), lte – less than and equal (<=)
        :return: The order id.
        """
        return call_sync(self.request_impl.create_order(symbol, account_type, order_type, amount, price, client_order_id, stop_price, operator))

    def batch_create_order(self, order_config_list) -> int:
        """
        Make an order in huobi.
        :param order_config_list: order config list, it can batch create orders, and each order config check as below
            : items as below
                :param symbol: The symbol, like "btcusdt". (mandatory)
                :param account_type: Account type. (mandatory)
                :param order_type: The order type. (mandatory)
                :param amount: The amount to buy (quote currency) or to sell (base currency). (mandatory)
                :param price: The limit price of limit order, only needed for limit order. (mandatory for buy-limit, sell-limit, buy-limit-maker and sell-limit-maker)
                :param client_order_id: unique Id which is user defined and must be unique in recent 24 hours
                :param stop_price: Price for auto sell to get the max benefit
                :param operator: the condition for stop_price, value can be "gte" or "lte",  gte – greater than and equal (>=), lte – less than and equal (<=)
        :return: The order id.
        """
        return call_sync(self.request_impl.batch_create_order(order_config_list))

    def get_open_orders(self, symbol: 'str', account_type: 'AccountType', side: 'OrderSide' = None,
                        size: 'int' = 100, from_id=None, direct=None) -> list:
        """
        The request of get open orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_type: account type, all defination to see AccountType in SDK. (mandatory)
        :param side: The order side, buy or sell. If no side defined, will return all open orders of the account. (optional)
        :param size: The number of orders to return. Range is [1, 500]. Default is 100. (optional)
        :param direct: 1:prev  order by ID asc from from_id, 2:next order by ID desc from from_id
        :param from_id: start ID for search
        :return: The orders information.
        """
        return call_sync(self.request_impl.get_open_orders(symbol, account_type, size, side, from_id, direct))

    def cancel_order(self, symbol: object, order_id: object) -> object:
        """
        Submit cancel request for cancelling an order.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id: The order id. (mandatory)
        :return: No return
        """
        call_sync(self.request_impl.cancel_order(symbol, order_id))

    def cancel_orders(self, order_id_list: 'list', client_order_id_list: 'list') -> None:
        """
        Submit cancel request for cancelling multiple orders.

        :param order_id_list: The list of order id. the max size is 50. (optional, but order_id_list or client_order_id_list only one is mandatory)
        :param client_order_id_list: The list of client order id. the max size is 50. (optional, but order_id_list or client_order_id_list only one is mandatory)
        :return: No return
        """
        return call_sync(self.request_impl.cancel_orders(order_id_list, client_order_id_list))

    def cancel_open_orders(self, symbol: 'str', account_type: 'AccountType', side: 'OrderSide' = None,
                           size: 'int' = None) -> BatchCancelResult:
        """
        Request to cancel open orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_type: Account type. (mandatory)
        :param side: The order side, buy or sell. If no side defined, will cancel all open orders of the account. (optional)
        :param size: The number of orders to cancel. Range is [1, 100]. Default is 100. (optional)
        :return: Status of batch cancel result.
        """
        return call_sync(self.request_impl.cancel_open_orders(symbol, account_type, side, size))

    def cancel_client_order(self, client_order_id: 'str') -> None:
        """
        Request to cancel open orders.

        :param client_order_id: user defined unique order id
        """
        return call_sync(self.request_impl.cancel_client_order(client_order_id))

    def get_order(self, symbol: 'str', order_id: 'int') -> Order:
        """
        Get the details of an order.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id: The order id. (mandatory)
        :return: The information of order.
        """
        return call_sync(self.request_impl.get_order(symbol, order_id))

    def get_order_by_client_order_id(self, client_order_id: 'str') -> Order:
        """
        Get the details of an order.

        :param client_order_id: The user defined unique order id. (mandatory)
        :return: The information of order.
        """
        return call_sync(self.request_impl.get_order_by_client_order_id(client_order_id))

    def get_match_results_by_order_id(self, order_id: 'int') -> list:
        """
        Get detail match results of an order.

        :param order_id: The order id. (mandatory)
        :return: The list of match result.
        """
        return call_sync(self.request_impl.get_match_results_by_order_id(order_id))

    def get_match_result(self, symbol: 'str', order_type: 'OrderSide' = None, start_date: 'str' = None,
                         end_date: 'str' = None,
                         size: 'int' = None,
                         from_id: 'int' = None,
                         direct:'str'=None):
        """
        Search for the trade records of an account.

        :param symbol: The symbol, like "btcusdt" (mandatory).
        :param order_type: The types of order to include in the search (optional).
        :param start_date: Search starts date in format yyyy-mm-dd. (optional).
        :param end_date: Search ends date in format yyyy-mm-dd. (optional).
        :param size: The number of orders to return, range [1-100] default is 100. (optional).
        :param from_id: Search order id to begin with. (optional).
        :return:
        """
        return call_sync(self.request_impl.get_match_results(symbol, order_type, start_date, end_date, size, from_id, direct))

    def withdraw(self, address: 'str', amount: 'float', currency: 'str', fee: 'float' = None,
                 address_tag: 'str' = None) -> int:
        """
        Submit a request to withdraw some asset from an account.

        :param address: The destination address of this withdraw. (mandatory)
        :param amount: The amount of currency to withdraw. (mandatory)
        :param currency: The crypto currency to withdraw. (mandatory)
        :param fee: The fee to pay with this withdraw. (optional)
        :param address_tag: A tag specified for this address. (optional)
        :return: Withdraw id
        """
        return call_sync(self.request_impl.withdraw(address, amount, currency, fee, address_tag))

    def cancel_withdraw(self, currency: 'str', withdraw_id: 'int') -> None:
        """
        Cancel an withdraw request.

        :param currency: The currency, like "btc". (mandatory)
        :param withdraw_id: withdraw id (mandatory)
        :return: No return.
        """
        call_sync(self.request_impl.cancel_withdraw(currency, withdraw_id))

    def get_historical_orders(self, symbol: 'str', order_state: 'OrderState', order_type: 'OrderType' = None,
                              start_date: 'str' = None, end_date: 'str' = None, start_id: 'int' = None,
                              size: 'int' = None, start_time:'int'=None, end_time:'int'=None) -> list:
        """
        Get historical orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_state: Order state , SUBMITTED etc. (mandatory)
        :param order_type: Order type. (optional)
        :param start_date: Start date in format yyyy-mm-dd. (optional)
        :param end_date: End date in format yyyy-mm-dd. (optional)
        :param start_id: Start id. (optional)
        :param size: The size of orders. (optional)
        :param start_time: millseconds time. (optional)
        :param end_time: millseconds time and (end_time - start_time) must less than 48 hours. (optional)
        :return:
        """
        return call_sync(
            self.request_impl.get_historical_orders(symbol, order_state, order_type, start_date, end_date, start_id,
                                                    size, start_time, end_time))

    def transfer_between_parent_and_sub(self, sub_uid: 'int', currency: 'str', amount: 'float',
                                        transfer_type: 'TransferMasterType'):
        """
        Transfer Asset between Parent and Sub Account.

        :param sub_uid: The target sub account uid to transfer to or from. (mandatory)
        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, see {@link TransferMasterType} (mandatory)
        :return: The order id.
        """
        return call_sync(self.request_impl.transfer_between_parent_and_sub(sub_uid, currency, amount, transfer_type))

    def get_current_user_aggregated_balance(self):
        """
        Get the aggregated balance of all sub-accounts of the current user.

        :return: The balance of all the sub-account aggregated.
        """
        return call_sync(self.request_impl.get_current_user_aggregated_balance())

    def get_specify_account_balance(self, sub_id):
        """
        Get account balance of a sub-account.

        :param sub_id: the specified sub account id to get balance for.
        :return: the balance of a sub-account specified by sub-account uid.
        """
        return call_sync(self.request_impl.get_specify_account_balance(sub_id))

    def get_etf_swap_config(self, etf_symbol: 'str') -> EtfSwapConfig:
        """
        Get the basic information of ETF creation and redemption, as well as ETF constituents,
        including max amount of creation, min amount of creation, max amount of redemption, min amount
        of redemption, creation fee rate, redemption fee rate, eft create/redeem status.

        :param etf_symbol: The symbol, currently only support hb10. (mandatory)
        :return: The etf configuration information.
        """
        return call_sync(self.request_impl.get_etf_swap_config(etf_symbol))

    def etf_swap(self, etf_symbol: 'str', amount: 'int', swap_type: 'EtfSwapType') -> None:
        """
        Order creation or redemption of ETF.

        :param etf_symbol: The symbol, currently only support hb10. (mandatory)
        :param amount: The amount to create or redemption. (mandatory)
        :param swap_type: The swap type to indicate creation or redemption. (mandatory)
        :return: No return
        """
        return call_sync(self.request_impl.etf_swap(etf_symbol, amount, swap_type))

    def get_etf_swap_history(self, etf_symbol: 'str', offset: 'int', size: 'int') -> list:
        """
        Get past creation and redemption.(up to 100 records)

        :param etf_symbol: The symbol, currently only support hb10. (mandatory)
        :param offset: The offset of the records, set to 0 for the latest records. (mandatory)
        :param size: The number of records to return, the range is [1, 100]. (mandatory)
        :return: The swap history.
        """
        return call_sync(self.request_impl.get_etf_swap_history(etf_symbol, offset, size))

    def get_etf_candlestick(self, etf_symbol: 'str', interval: 'CandlestickInterval', size: 'int'=None) -> list:
        """
        Get the latest candlestick/kline for the etf.

        :param etf_symbol: The symbol, currently only support hb10. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The maximum number of candlestick/kline requested. Range [1 - 2000] (optional)
        :return: The list of candlestick/kline data.
        """
        return call_sync(self.request_impl.get_etf_candlestick(etf_symbol, interval, size))

    def get_margin_balance_detail(self, symbol: 'str' = None, sub_uid: 'int' = None) -> list:
        """
        Get the Balance of the Margin Loan Account.

        :param symbol: The currency, like "trxusdt". (optional)
        :param sub_uid: The currency for specific user. (optional)
        :return: The margin loan account detail list.
        """
        return call_sync(self.request_impl.get_margin_balance_detail(symbol, sub_uid))

    def get_fee_rate(self, symbols: 'str') -> list:
        """
        The request of get open orders.

        :param symbols: The symbol, like "btcusdt,htusdt". (mandatory)
        :return: The fee information.
        """
        return call_sync(self.request_impl.get_fee_rate(symbols))

    def get_margin_loan_info(self, symbols: 'str'=None) -> list:
        """
        The request of get margin loan info, can return currency loan info list.

        :param symbols: The symbol, like "btcusdt,htusdt". (optional)
        :return: The cross margin loan info.
        """
        return call_sync(self.request_impl.get_margin_loan_info(symbols))

    def get_cross_margin_loan_info(self) -> list:
        """
        The request of currency loan info list.

        :return: The cross margin loan info list.
        """
        return call_sync(self.request_impl.get_cross_margin_loan_info())

    def get_reference_transact_fee_rate(self, symbols: 'str') -> list:
        """
        The request of get transact fee rate list.

        :param symbols: The symbol, like "btcusdt,htusdt". (mandatory)
        :return: The transact fee rate list.
        """
        return call_sync(self.request_impl.get_reference_transact_fee_rate(symbols))


    def transfer_between_futures_and_pro(self, currency: 'str', amount: 'float',
                                        transfer_type: 'TransferFuturesPro')-> int:
        """
        Transfer Asset between Futures and Contract.

        :param sub_uid: The target sub account uid to transfer to or from. (mandatory)
        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, need be "futures-to-pro" or "pro-to-futures" (mandatory)
        :return: The order id.
        """
        return call_sync(self.request_impl.transfer_between_futures_and_pro(currency, amount, transfer_type))

    def get_order_in_recent_48hour(self, symbol=None, start_time=None, end_time=None, size=None, direct=None)-> list:
        """
        Transfer Asset between Futures and Contract.

        :param direct:
        :param symbol: The target sub account uid to transfer to or from. (mandatory)
        :param start_time: The crypto currency to transfer. (mandatory)
        :param end_time: The amount of asset to transfer. (mandatory)
        :param size: The type of transfer, need be "futures-to-pro" or "pro-to-futures" (mandatory)
        :return: The Order list.
        """
        return call_sync(self.request_impl.get_order_in_recent_48hour(symbol, start_time, end_time, size, direct))


    def get_reference_currencies(self, currency:'str'=None, is_authorized_user:'bool' =None) ->list:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :param currency: btc, ltc, bch, eth, etc ...(available currencies in Huobi Global)
        :param is_authorized_user: is Authorized user? True or False
        :return: The information of trading instrument and currencies.
        """
        return call_sync(self.request_impl.get_reference_currencies(currency, is_authorized_user))

    def get_account_deposit_address(self, currency: 'str') ->list:
        """
        Get deposit address of corresponding chain, for a specific crypto currency (except IOTA)

        :param currency: The currency, like "btc". (optional)
        :return:
        """
        return call_sync(self.request_impl.get_account_deposit_address(currency))

    def get_account_withdraw_quota(self, currency: 'str')->list:
        """
        Get the withdraw quota for currencies

        :param currency: The currency, like "btc". (mandatory)
        :return:
        """
        return call_sync(self.request_impl.get_account_withdraw_quota(currency))

    def get_sub_user_deposit_address(self, sub_uid: 'int', currency: 'str') -> list:
        """
        Parent get sub user deposit address

        :param sub_uid: Sub user id
        :param currency: Cryptocurrency, like "btc". (mandatory)
        :return:
        """
        return call_sync(self.request_impl.get_sub_user_deposit_address(sub_uid, currency))

    def get_deposit_withdraw(self, op_type:'str', currency: 'str'=None, from_id: 'int'=None, size: 'int'=None, direct:'str'=None) -> list:
        """
        Get the withdraw records of an account.

        :param currency: The currency, like "btc". (optional)
        :param from_id: The beginning withdraw record id. (optional)
        :param op_type: deposit or withdraw, see defination DepositWithdraw (mandatory)
        :param size: The size of record. (optional)
        :param direct: "prev" is order by asc, "next" is order by desc, default as "prev"(optional)
        :return: The list of withdraw records.
        """
        return call_sync(self.request_impl.get_deposit_withdraw(op_type, currency, from_id, size, direct))


    def post_create_withdraw(self, address: 'str', amount: 'float', currency: 'str', fee: 'float',
                 chain:'str' =None, address_tag: 'str' = None) -> int:
        """
        Submit a request to withdraw some asset from an account.

        :param address: The destination address of this withdraw. (mandatory)
        :param amount: The amount of currency to withdraw. (mandatory)
        :param currency: The crypto currency to withdraw. (mandatory)
        :param fee: The fee to pay with this withdraw. (mandatory)
        :param address_tag: A tag specified for this address. (optional)
        :param chain: set as "usdt" to withdraw USDT to OMNI, set as "trc20usdt" to withdraw USDT to TRX. (optional)
        :return: Withdraw id
        """
        return call_sync(self.request_impl.post_create_withdraw(address, amount, currency, fee, chain, address_tag))

    def post_cancel_withdraw(self, withdraw_id: 'int') -> int:
        """
        Cancel an withdraw request.

        :param withdraw_id: withdraw id (mandatory)
        :return: No return.
        """
        return call_sync(self.request_impl.post_cancel_withdraw(withdraw_id))

    def post_cross_margin_transfer_in(self, currency: 'str', amount:'float') -> int:
        """
        transfer currency to cross account.

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return transfer id.
        """
        return call_sync(self.request_impl.post_cross_margin_transfer_in(currency, amount))

    def post_cross_margin_transfer_out(self, currency: 'str', amount:'float') -> int:
        """
        transfer currency out from cross account.

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return transfer id.
        """
        return call_sync(self.request_impl.post_cross_margin_transfer_out(currency, amount))

    def post_cross_margin_create_loan_orders(self, currency:'str', amount: 'float') -> int:
        """
        create cross margin loan orders

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return order id.
        """
        return call_sync(self.request_impl.post_cross_margin_create_loan_orders(currency, amount))

    def post_cross_margin_loan_order_repay(self, order_id:'str', amount: 'float'):
        """
        repay cross margin loan orders

        :param currency: currency name (mandatory)
        :param amount: transfer amount (mandatory)
        :return: return order id.
        """
        return call_sync(self.request_impl.post_cross_margin_loan_order_repay(order_id, amount))

    def get_cross_margin_loan_orders(self, currency:'str'=None, state:'str'=None,
                                     start_date:'str'=None, end_date:'str'=None,
                                     from_id:'int'=None, size:'int'=None, direct:'str'=None, sub_uid:'int'=None) -> list:
        """
        get cross margin loan orders

        :return: return list.
        """
        return call_sync(self.request_impl.get_cross_margin_loan_orders(currency, state, start_date, end_date, from_id, size, direct, sub_uid))

    def get_cross_margin_account_balance(self, sub_uid:'int'=None):
        """
        get cross margin account balance

        :return: cross-margin account.
        """
        return call_sync(self.request_impl.get_cross_margin_account_balance(sub_uid))

    def get_account_history(self, account_id:'int', currency:'str'=None,
                            transact_types:'str'=None, start_time:'int'=None, end_time:'int'=None,
                            sort:'str'=None, size:'int'=None):
        """
        get account change record

        :return: account change record list.
        """
        return call_sync(self.request_impl.get_account_history(account_id, currency,
                            transact_types, start_time, end_time,
                            sort, size))


    def sub_uid_management(self, sub_uid:'int', action:'str'):
        """
        get account change record

        :return: account change record list.
        """
        return call_sync(self.request_impl.sub_user_management(sub_uid, action))

    def get_market_tickers(self) -> list:
        """
        get market tickers

        :return: market ticker list.
        """
        return call_sync(self.request_impl.get_market_tickers())

    def get_account_ledger(self, account_id:'int', currency:'str'=None, transact_types:'str'=None,
                           start_time:'int'=None, end_time:'int'=None, sort:'str'=None, limit:'int'=None,
                           from_id:'int'=None) -> list:
        """
        get account ledger

        :return: account ledger list.
        """
        return call_sync(self.request_impl.get_account_ledger(account_id, currency, transact_types, start_time, end_time, sort, limit, from_id))

    def get_system_status(self) -> str:
        """
        get system status

        :return: system status.
        """
        return call_sync(self.request_impl.get_system_status(), is_checked=True)
