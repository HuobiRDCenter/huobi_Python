from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.restapiinvoker import call_sync
from huobi.impl.accountinfomap import account_info_map
from huobi.impl.utils.inputchecker import *
from huobi.model import *


class RequestClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        api_key = None
        secret_key = None
        url = "https://api.hbdm.com"
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            secret_key = kwargs["secret_key"]
        if "url" in kwargs:
            url = kwargs["url"]
        try:
            self.request_impl = RestApiRequestImpl(api_key, secret_key, url)
            account_info_map.update_user_info(api_key, self.request_impl)
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

    def get_withdraw_history(self, currency: 'str', from_id: 'int', size: 'int') -> list:
        """
        Get the withdraw records of an account.

        :param currency: The currency, like "btc". (mandatory)
        :param from_id: The beginning withdraw record id. (mandatory)
        :param size: The size of record. (mandatory)
        :return: The list of withdraw records.
        """
        return call_sync(self.request_impl.get_withdraw_history(currency, from_id, size))

    def get_deposit_history(self, currency: 'str', from_id: 'int', size: 'int') -> list:
        """
        Get the deposit records of an account.

        :param currency: The currency, like "btc". (mandatory)
        :param from_id: The beginning deposit record id. (mandatory)
        :param size: The size of record. (mandatory)
        :return: The list of deposit records.
        """
        return call_sync(self.request_impl.get_deposit_history(currency, from_id, from_id, size))

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

    def get_account_balance(self) -> list:
        """
        Get the balance of a all accounts.

        :return: The information of all account balance.
        """
        accounts = call_sync(self.request_impl.get_accounts())
        for item in accounts:
            balances = call_sync(self.request_impl.get_balance(item))
            item.balances = balances
        return accounts

    def get_account_balance_by_account_type(self, account_type: "AccountType") -> Account:
        """
        Get the balance of a all accounts or specified account.

        :param account_type: The specified account type. if it is not filled, this method will return all accounts (mandatory)
        :return: The information of the account that is specified type.
        """
        check_should_not_none(account_type, "account_type")
        accounts = call_sync(self.request_impl.get_accounts())
        for item in accounts:
            if account_type == item.account_type:
                balances = call_sync(self.request_impl.get_balance(item))
                item.balances = balances
                return item

    def create_order(self, symbol: 'str', account_type: 'AccountType', order_type: 'OrderType', amount: 'float',
                     price: 'float') -> int:
        """
        Make an order in huobi.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_type: Account type. (mandatory)
        :param order_type: The order type. (mandatory)
        :param amount: The amount to buy (quote currency) or to sell (base currency). (mandatory)
        :param price: The limit price of limit order, only needed for limit order. (mandatory for buy-limit, sell-limit, buy-limit-maker and sell-limit-maker)
        :return: The order id.
        """
        return call_sync(self.request_impl.create_order(symbol, account_type, order_type, amount, price))

    def create_contract_order(self, symbol: 'str'
                     , contract_type: 'ContractType'
                     , contract_code: 'str'
                     , client_order_id: 'str'
                     , price: 'float'
                     , volume: 'long'
                     , direction: 'TradeDirection'
                     , offset: 'TradeOffset'
                     , lever_rate: 'str'
                     , order_price_type: 'str'
                     ) -> int:
        """
        symbol	            string	true	"BTC","ETH"...
        contract_type	    string	true	合约类型 ("this_week":当周 "next_week":下周 "quarter":季度)
        contract_code	    string	true	BTC180914
        client_order_id	    long	false	客户自己填写和维护，这次一定要大于上一次
        price	            decimal	true	价格
        volume	            long	true	委托数量(张)
        direction	        string	true	"buy":买 "sell":卖
        offset	            string	true	"open":开 "close":平
        lever_rate	        int	    true	杠杆倍数[“开仓”若有10倍多单，就不能再下20倍多单]
        order_price_type	string	true	订单报价类型 "limit":限价 "opponent":对手价 "post_only":只做Maker单
        """
        return call_sync(self.request_impl.create_contract_order(symbol, contract_type, contract_code, client_order_id, price, volume, direction, offset, lever_rate, order_price_type))

    def cancel_contract_all(self
                            , symbol
                            , contract_code
                            , contract_type: 'ContractType'
                              ) -> int:
        """
        symbol	        true	string	品种代码，如"BTC","ETH"...
        contract_code	false	string	合约code
        contract_type	false	string	合约类型
        """
        return call_sync(self.request_impl.cancel_contract_all(symbol, contract_code, contract_type))

    def get_contract_orders(self
                            , order_id
                            , client_order_id
                            , symbol: 'str'
                            ) -> int:
        """
        order_id	false	string	订单ID(多个订单ID中间以","分隔,一次最多允许查询20个订单)
        client_order_id	false	string	客户订单ID(多个订单ID中间以","分隔,一次最多允许查询20个订单)
        symbol	true	string	"BTC","ETH"...
        """
        return call_sync(self.request_impl.get_contract_orders(order_id, client_order_id, symbol))

    def get_open_orders(self, symbol: 'str', account_type: 'AccountType', side: 'OrderSide' = None,
                        size: 'int' = 10) -> list:
        """
        The request of get open orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_type: The order side, buy or sell. If no side defined, will return all open orders of the account. (mandatory)
        :param side: The order side, buy or sell. If no side defined, will return all open orders of the account. (optional)
        :param size: The number of orders to return. Range is [1, 500]. Default is 10. (optional)
        :return: The orders information.
        """
        return call_sync(self.request_impl.get_open_orders(symbol, account_type, size, side))

    def cancel_order(self, symbol: object, order_id: object) -> object:
        """
        Submit cancel request for cancelling an order.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id: The order id. (mandatory)
        :return: No return
        """
        call_sync(self.request_impl.cancel_order(symbol, order_id))

    def cancel_orders(self, symbol: 'str', order_id_list: 'list') -> None:
        """
        Submit cancel request for cancelling multiple orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id_list: The list of order id. the max size is 50. (mandatory)
        :return: No return
        """
        call_sync(self.request_impl.cancel_orders(symbol, order_id_list))

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

    def get_order(self, symbol: 'str', order_id: 'int') -> Order:
        """
        Get the details of an order.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id: The order id. (mandatory)
        :return: The information of order.
        """
        return call_sync(self.request_impl.get_order(symbol, order_id))

    def get_match_results_by_order_id(self, symbol: 'str', order_id: 'int') -> list:
        """
        Get detail match results of an order.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id: The order id. (mandatory)
        :return: The list of match result.
        """
        return call_sync(self.request_impl.get_match_results_by_order_id(symbol, order_id))

    def get_match_result(self, symbol: 'str', order_type: 'OrderSide' = None, start_date: 'str' = None,
                         end_date: 'str' = None,
                         size: 'int' = None,
                         from_id: 'int' = None):
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
        return call_sync(self.request_impl.get_match_results(symbol, order_type, start_date, end_date, size, from_id))

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
                              size: 'int' = None) -> list:
        """
        Get historical orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_state: Order state , SUBMITTED etc. (mandatory)
        :param order_type: Order type. (optional)
        :param start_date: Start date in format yyyy-mm-dd. (optional)
        :param end_date: End date in format yyyy-mm-dd. (optional)
        :param start_id: Start id. (optional)
        :param size: The size of orders. (optional)
        :return:
        """
        return call_sync(
            self.request_impl.get_historical_orders(symbol, order_state, order_type, start_date, end_date, start_id,
                                                    size))

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
        return call_sync(self.request_impl.get_etf_swap_config(etf_symbol, offset, size))

    def get_etf_candlestick(self, etf_symbol: 'str', interval: 'CandlestickInterval', size: 'int' = None) -> list:
        """
        Get the latest candlestick/kline for the etf.

        :param etf_symbol: The symbol, currently only support hb10. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The maximum number of candlestick/kline requested. Range [1 - 2000] (optional)
        :return: The list of candlestick/kline data.
        """
        return call_sync(self.request_impl.get_etf_candlestick(etf_symbol, interval, size))

    def get_margin_balance_detail(self, symbol: 'str') -> list:
        """
        Get the Balance of the Margin Loan Account.

        :param symbol: The currency, like "btc". (mandatory)
        :return: The margin loan account detail list.
        """
        return call_sync(self.request_impl.get_margin_balance_detail(symbol))
