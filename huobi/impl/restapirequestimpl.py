from huobi.impl import RestApiRequest
from huobi.impl.utils.apisignaturev2 import create_signature_v2
from huobi.impl.utils.urlparamsbuilder import UrlParamsBuilder
from huobi.impl.utils.apisignature import create_signature
from huobi.impl.accountinfomap import account_info_map
from huobi.impl.utils.inputchecker import *
from huobi.impl.utils.timeservice import *
from huobi.model import *
from huobi.model.accountledger import AccountLedger
from huobi.model.deposithistory import DepositHistory, History
from huobi.model.feerate import FeeRate
from huobi.model.marketticker import MarketTicker


class RestApiRequestImpl(object):
    # __MARKET_URL = "https://api.huobi.pro:443"
    # __TRADING_URL = "https://api.huobi.pro:443"

    def list_remove_duplicate(self, lst1):
        lst2 = sorted(set(lst1), key=lst1.index)
        return lst2

    def __init__(self, api_key, secret_key, server_url="https://api.huobi.pro"):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__server_url = server_url

    def __create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({'Content-Type': 'application/json'})
        if (len(builder.post_list)):  # specify for case : /v1/order/batch-orders
            request.post_body = builder.post_list
        else:
            request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({"Content-Type": "application/x-www-form-urlencoded"})
        request.url = url + builder.build_url()
        return request

    def get_exchange_timestamp(self):
        request = self.__create_request_by_get("/v1/common/timestamp", UrlParamsBuilder())

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_candlestick(self, symbol, interval, size, start_time=None, end_time=None):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")

        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("period", interval)
        builder.put_url("size", size)
        builder.put_url("start_time", start_time)
        builder.put_url("end_time", end_time)

        request = self.__create_request_by_get("/market/history/kline", builder)

        def parse(json_wrapper):
            candlestick_list = list()
            data_list = json_wrapper.get_array("data")
            for item in data_list.get_items():
                candlestick = Candlestick.json_parse(item)
                candlestick_list.append(candlestick)
            return candlestick_list

        request.json_parser = parse
        return request

    def get_price_depth(self, symbol, size=None):
        check_symbol(symbol)
        check_range(size, 1, 150, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("type", "step0")
        request = self.__create_request_by_get("/market/depth", builder)

        def parse(json_wrapper):
            tick = json_wrapper.get_object("tick")
            dp = PriceDepth()
            dp.timestamp = tick.get_int("ts")
            bid_array = tick.get_array("bids")
            ask_array = tick.get_array("asks")
            bids = list()
            asks = list()
            for i in range(0, size):
                bid_entry = bid_array.get_array_at(i)
                entry = DepthEntry()
                entry.price = bid_entry.get_float_at(0)
                entry.amount = bid_entry.get_float_at(1)
                bids.append(entry)
            for i in range(0, size):
                ask_entry = ask_array.get_array_at(i)
                entry = DepthEntry()
                entry.price = ask_entry.get_float_at(0)
                entry.amount = ask_entry.get_float_at(1)
                asks.append(entry)
            dp.bids = bids
            dp.asks = asks
            return dp

        request.json_parser = parse
        return request

    def get_market_trade(self, symbol):
        check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        request = self.__create_request_by_get("/market/trade", builder)

        def parse(json_wrapper):
            tick_obj = json_wrapper.get_object("tick")
            data_array = tick_obj.get_array("data")
            trade_list = list()

            for item in data_array.get_items():
                local_trade = Trade.json_parse(item)
                trade_list.append(local_trade)

            return trade_list

        request.json_parser = parse
        return request

    def get_historical_trade(self, symbol, form_id, size):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("size", size)
        request = self.__create_request_by_get("/market/history/trade", builder)

        def parse(json_wrapper):
            data_array = json_wrapper.get_array("data")
            trade_list = list()
            for item in data_array.get_items():
                data_array_in = item.get_array("data")
                for item_in in data_array_in.get_items():
                    local_trade = Trade.json_parse(item_in)
                    trade_list.append(local_trade)
            return trade_list

        request.json_parser = parse
        return request

    def get_24h_trade_statistics(self, symbol):
        check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        request = self.__create_request_by_get("/market/detail", builder)

        def parse(json_wrapper):
            tick = json_wrapper.get_object("tick")
            trade_statistics = TradeStatistics()
            trade_statistics.timestamp = json_wrapper.get_int("ts")
            trade_statistics.amount = tick.get_float("amount")
            trade_statistics.open = tick.get_float("open")
            trade_statistics.close = tick.get_float("close")
            trade_statistics.high = tick.get_float("high")
            trade_statistics.low = tick.get_float("low")
            trade_statistics.count = tick.get_int("count")
            trade_statistics.volume = tick.get_float("vol")
            return trade_statistics

        request.json_parser = parse
        return request

    def get_symbols(self):
        request = self.__create_request_by_get("/v1/common/symbols", UrlParamsBuilder())

        def parse(json_wrapper):
            symbols = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                local_symbol = Symbol()
                local_symbol.base_currency = item.get_string("base-currency")
                local_symbol.quote_currency = item.get_string("quote-currency")
                local_symbol.price_precision = item.get_int("price-precision")
                local_symbol.amount_precision = item.get_int("amount-precision")
                local_symbol.symbol_partition = item.get_string("symbol-partition")
                local_symbol.symbol = item.get_string("symbol")
                local_symbol.state = item.get_string("state")
                local_symbol.value_precision = item.get_string("value-precision")
                local_symbol.min_order_amt = item.get_string("min-order-amt")
                local_symbol.max_order_amt = item.get_string("max-order-amt")
                local_symbol.min_order_value = item.get_string("min-order-value")
                local_symbol.leverage_ratio = item.get_string_or_default("leverage-ratio", 0)
                symbols.append(local_symbol)
            return symbols

        request.json_parser = parse
        return request

    def get_currencies(self):
        request = self.__create_request_by_get("/v1/common/currencys", UrlParamsBuilder())

        def parse(json_wrapper):
            return json_wrapper.get_array("data").get_items_as_string()

        request.json_parser = parse
        return request

    def get_best_quote(self, symbol):
        check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        request = self.__create_request_by_get("/market/detail/merged", builder)

        def parse(json_wrapper):
            best_quote = BestQuote()
            best_quote.timestamp = json_wrapper.get_int("ts")
            tick = json_wrapper.get_object("tick")
            ask_array = tick.get_array("ask")
            best_quote.ask_price = ask_array.get_float_at(0)
            best_quote.ask_amount = ask_array.get_float_at(1)
            bid_array = tick.get_array("bid")
            best_quote.bid_price = bid_array.get_float_at(0)
            best_quote.bid_amount = bid_array.get_float_at(1)
            return best_quote

        request.json_parser = parse
        return request

    def get_accounts(self):
        request = self.__create_request_by_get_with_signature("/v1/account/accounts", UrlParamsBuilder())

        def parse(json_wrapper):
            account_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                account = Account()
                account.id = item.get_int("id")
                account.account_type = item.get_string("type")
                account.account_state = item.get_string("state")
                account.subtype = item.get_string_or_default("subtype", "")
                account_list.append(account)
            return account_list

        request.json_parser = parse
        return request

    def get_withdraw_history(self, currency, from_id, size, direct):
        check_should_not_none(from_id, "from_id")
        check_should_not_none(size, "size")

        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("type", DepositWithdraw.WITHDRAW)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        builder.put_url("direct", direct)
        request = self.__create_request_by_get_with_signature("/v1/query/deposit-withdraw", builder)

        def parse(json_wrapper):
            withdraws = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                withdraw = Withdraw()
                withdraw.id = item.get_int("id")
                withdraw.currency = item.get_string("currency")
                withdraw.tx_hash = item.get_string("tx-hash")
                withdraw.amount = item.get_float("amount")
                withdraw.address = item.get_string("address")
                withdraw.address_tag = item.get_string("address-tag")
                withdraw.fee = item.get_float("fee")
                withdraw.type = item.get_string("type")
                withdraw.chain = item.get_string("chain")
                withdraw.withdraw_state = item.get_string("state")
                withdraw.created_timestamp = item.get_int("created-at")
                withdraw.updated_timestamp = item.get_int("updated-at")
                withdraws.append(withdraw)
            return withdraws

        request.json_parser = parse
        return request

    def get_deposit_history(self, currency, from_id, size, direct):
        check_should_not_none(from_id, "from_id")
        check_should_not_none(size, "size")

        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("type", DepositWithdraw.DEPOSIT)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        builder.put_url("direct", direct)
        request = self.__create_request_by_get_with_signature("/v1/query/deposit-withdraw", builder)

        def parse(json_wrapper):
            deposits = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                deposit = Deposit()
                deposit.id = item.get_int("id")
                deposit.currency = item.get_string("currency")
                deposit.tx_hash = item.get_string("tx-hash")
                deposit.amount = item.get_float("amount")
                deposit.address = item.get_string("address")
                deposit.address_tag = item.get_string("address-tag")
                deposit.fee = item.get_float("fee")
                deposit.type = item.get_string("type")
                deposit.chain = item.get_string("chain")
                deposit.withdraw_state = item.get_string("state")
                deposit.created_timestamp = item.get_int("created-at")
                deposit.updated_timestamp = item.get_int("updated-at")
                deposits.append(deposit)
            return deposits

        request.json_parser = parse
        return request

    def get_sub_user_deposit_history(self, sub_uid, currency=None, start_time=None, end_time=None, sort=None, limit=None, from_id=None):
        check_should_not_none(sub_uid, "sub_uid")

        builder = UrlParamsBuilder()
        builder.put_url("subUid", sub_uid)
        builder.put_url("currency", currency)
        builder.put_url("startTime", start_time)
        builder.put_url("endTime", end_time)
        builder.put_url("sort", sort)
        builder.put_url("limit", limit)
        builder.put_url("fromId", from_id)
        request = self.__create_request_by_get_with_signature("/v2/sub-user/query-deposit", builder)

        def parse(json_wrapper):
            deposit_history = DepositHistory()
            deposit_history.nextId = json_wrapper.get_int_or_default("nextId", 0)
            deposit_history.data = list()
            list_array = json_wrapper.get_array("data")
            for item in list_array.get_items():
                history = History()
                history.id = item.get_int("id")
                history.currency = item.get_string("currency")
                history.txHash = item.get_string("txHash")
                history.amount = item.get_float("amount")
                history.address = item.get_string("address")
                history.addressTag = item.get_string("addressTag")
                history.deposit_state = item.get_string("state")
                history.created_timestamp = item.get_int("createTime")
                history.updated_timestamp = item.get_int("updateTime")
                deposit_history.data.append(history)
            return deposit_history

        request.json_parser = parse
        return request

    def get_balance(self, account):
        path = "/v1/account/accounts/{}/balance"
        path = path.format(account.id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            balances = list()
            data = json_wrapper.get_object("data")
            list_array = data.get_array("list")
            for item in list_array.get_items():
                balance = Balance()
                balance.balance = item.get_float("balance")
                balance.currency = item.get_string("currency")
                balance.balance_type = item.get_string("type")
                balances.append(balance)
            return balances

        request.json_parser = parse
        return request

    def transfer(self, symbol, from_account, to_account, currency, amount):
        check_symbol(symbol)
        check_should_not_none(from_account, "from_account")
        check_should_not_none(to_account, "to_account")
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        if from_account == AccountType.SPOT and to_account == AccountType.MARGIN:
            address = "/v1/dw/transfer-in/margin"
        elif from_account == AccountType.MARGIN and AccountType.SPOT:
            address = "/v1/dw/transfer-out/margin"
        else:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] incorrect transfer type")
        builder = UrlParamsBuilder()
        builder.put_post("currency", currency)
        builder.put_post("symbol", symbol)
        builder.put_post("amount", amount)
        request = self.__create_request_by_post_with_signature(address, builder)

        def parse(json_wrapper):
            if json_wrapper.get_string("status") == "ok":
                return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def apply_loan(self, symbol, currency, amount):
        check_symbol(symbol)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("currency", currency)
        builder.put_post("symbol", symbol)
        builder.put_post("amount", amount)
        request = self.__create_request_by_post_with_signature("/v1/margin/orders", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def repay_loan(self, load_id, amount):
        check_should_not_none(load_id, "load_id")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        path = "/v1/margin/orders/{}/repay"
        path = path.format(load_id)
        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_loan(self, symbol, start_date=None, end_date=None, states=None, from_id=None, size=None, direction=None):
        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("states", states)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        builder.put_url("direct", direction)
        request = self.__create_request_by_get_with_signature("/v1/margin/loan-orders", builder)

        def parse(json_wrapper):
            loan_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                loan = Loan()
                loan.loan_balance = item.get_float("loan-balance")
                loan.interest_balance = item.get_float("interest-balance")
                loan.interest_rate = item.get_float("interest-rate")
                loan.loan_amount = item.get_float("loan-amount")
                loan.interest_amount = item.get_float("interest-amount")
                loan.symbol = item.get_string("symbol")
                loan.currency = item.get_string("currency")
                loan.id = item.get_int("id")
                loan.state = item.get_string("state")
                loan.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                       item.get_int("account-id")).account_type
                loan.user_id = item.get_int("user-id")

                loan.deduct_rate = item.get_float("deduct-rate")
                loan.paid_point = item.get_float("paid-point")
                loan.deduct_currency = item.get_string("deduct-currency")
                loan.account_id = item.get_int("account-id")
                loan.paid_coin = item.get_float("paid-coin")
                loan.deduct_amount = item.get_float("deduct-amount")

                loan.accrued_timestamp = item.get_int("accrued-at")
                loan.created_timestamp = item.get_int("created-at")
                loan.updated_timestamp = item.get_int("updated-at")
                loan_list.append(loan)
            return loan_list

        request.json_parser = parse
        return request

    @staticmethod
    def order_source_desc(account_type):
        default_source = OrderSource.API
        if account_type:
            if account_type == AccountType.MARGIN:
                return OrderSource.MARGIN_API
            if account_type == AccountType.SUPER_MARGIN:
                return OrderSource.SUPER_MARGIN_API
        return default_source

    def create_order(self, symbol, account_type, order_type, amount, price,
                     client_order_id=None, stop_price=None, operator=None):
        check_symbol(symbol)
        check_should_not_none(account_type, "account_type")
        check_should_not_none(order_type, "order_type")
        check_should_not_none(amount, "amount")
        need_checked_order_type_list = [OrderType.SELL_LIMIT, OrderType.BUY_LIMIT, OrderType.BUY_LIMIT_MAKER, OrderType.SELL_LIMIT_MAKER,
                                        OrderType.BUY_STOP_LIMIT, OrderType.SELL_STOP_LIMIT, OrderType.BUY_LIMIT_FOK, OrderType.SELL_LIMIT_FOK,
                                        OrderType.BUY_STOP_LIMIT_FOK, OrderType.SELL_STOP_LIMIT_FOK]
        if order_type in need_checked_order_type_list:
            check_should_not_none(price, "price")
        if order_type == OrderType.SELL_MARKET or order_type == OrderType.BUY_MARKET:
            price = None
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type=account_type, subtype=symbol)
        source = RestApiRequestImpl.order_source_desc(account_type)
        builder = UrlParamsBuilder()
        builder.put_post("account-id", account.id)
        builder.put_post("amount", amount)
        builder.put_post("price", price)
        builder.put_post("symbol", symbol)
        builder.put_post("type", order_type)
        builder.put_post("source", source)
        builder.put_post("client-order-id", client_order_id)
        builder.put_post("stop-price", stop_price)
        builder.put_post("operator", operator)

        request = self.__create_request_by_post_with_signature("/v1/order/orders/place", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def batch_create_order(self, create_params_list):
        check_should_not_none(create_params_list, "order_config_list")
        check_list(create_params_list, 1, 10, "create order config list")

        new_config_list = list()
        for item in create_params_list:
            symbol = item.get("symbol", None)
            account_type = item.get("account_type", None)
            order_type = item.get("order_type", None)
            amount = item.get("amount", None)
            price = None

            check_symbol(symbol)
            check_should_not_none(account_type, "account_type")
            check_should_not_none(order_type, "order_type")
            check_should_not_none(amount, "amount")
            need_checked_order_type_list = [OrderType.SELL_LIMIT, OrderType.BUY_LIMIT, OrderType.BUY_LIMIT_MAKER, OrderType.SELL_LIMIT_MAKER,
                                            OrderType.BUY_STOP_LIMIT, OrderType.SELL_STOP_LIMIT, OrderType.BUY_LIMIT_FOK, OrderType.SELL_LIMIT_FOK,
                                            OrderType.BUY_STOP_LIMIT_FOK, OrderType.SELL_STOP_LIMIT_FOK]
            if order_type in need_checked_order_type_list:
                check_should_not_none(item.get("price", None), "price for limit order")
                price = item.get("price", None)
            elif order_type == OrderType.SELL_MARKET or order_type == OrderType.BUY_MARKET:
                price = None


            global account_info_map
            user = account_info_map.get_user(self.__api_key)

            account = user.get_account_by_type(account_type=account_type, subtype=symbol)
            new_item = {
                'account-id' : account.id,
                "symbol" : symbol,
                'type' : order_type,
                'amount': amount,
                'price': price,
                'source': RestApiRequestImpl.order_source_desc(account_type=account_type)
            }

            client_order_id = item.get("client_order_id", None)
            if client_order_id:
                new_item['client-order-id'] = client_order_id

            stop_price = item.get("stop-price", None)
            if stop_price:
                new_item['stop-price'] = stop_price

            operator = item.get("operator", None)
            if operator:
                new_item['operator'] = operator

            new_config_list.append(new_item)

        builder = UrlParamsBuilder()
        builder.post_list = new_config_list

        request = self.__create_request_by_post_with_signature("/v1/order/batch-orders", builder)

        def parse(json_wrapper):
            create_result_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                item_obj = BatchCreateOrder.json_parse(item)
                create_result_list.append(item_obj)

            return create_result_list

        request.json_parser = parse
        return request

    def get_open_orders(self, symbol, account_type, size=None, side=None, from_id=None, direct=None):
        check_symbol(symbol)
        check_range(size, 1, 500, "size")
        check_should_not_none(account_type, "account_type")
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type=account_type, subtype=symbol)
        builder = UrlParamsBuilder()
        builder.put_url("account-id", account.id)
        builder.put_url("symbol", symbol)
        builder.put_url("side", side)
        builder.put_url("size", size)
        builder.put_url("from", from_id)
        builder.put_url("direct", direct)
        request = self.__create_request_by_get_with_signature("/v1/order/openOrders", builder)

        """
        def parse(json_wrapper):
            order_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                order = Order()
                order.order_id = item.get_int("id")
                order.symbol = item.get_string("symbol")
                order.price = item.get_float("price")
                order.amount = item.get_float("amount")
                order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                        item.get_int("account-id")).account_type
                order.created_timestamp = item.get_int("created-at")
                order.order_type = item.get_string("type")
                order.filled_amount = item.get_float("filled-amount")
                order.filled_cash_amount = item.get_float("filled-cash-amount")
                order.filled_fees = item.get_float("filled-fees")
                order.source = item.get_string("source")
                order.state = item.get_string("state")
                order_list.append(order)
            return order_list
        """

        request.json_parser = self.get_order_list_json_parse
        return request

    def cancel_order(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/{}/submitcancel"
        path = path.format(order_id)
        request = self.__create_request_by_post_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def cancel_orders(self, order_id_list_param, client_order_id_list_param):

        if (order_id_list_param is None or len(order_id_list_param) == 0) \
                and (client_order_id_list_param is None or len(client_order_id_list_param) == 0):
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] order_id_list or client_order_id_list must input only one")

        builder = UrlParamsBuilder()
        string_list = list()
        if len(order_id_list_param):
            order_id_list = self.list_remove_duplicate(order_id_list_param)
            check_list(order_id_list, 1, 50, "order_id_list")
            for order_id in order_id_list:
                string_list.append(str(order_id))

            builder.put_post("order-ids", string_list)
        elif len(client_order_id_list_param):
            client_order_id_list = self.list_remove_duplicate(client_order_id_list_param)
            check_list(client_order_id_list, 1, 50, "client_order_id_list")

            string_list = list()
            for order_id in client_order_id_list:
                string_list.append(str(order_id))
            builder.put_post("client-order-ids", string_list)

        request = self.__create_request_by_post_with_signature("/v1/order/orders/batchcancel", builder)

        def parse(json_wrapper):
            return BatchCancelOrder.json_parse(json_wrapper)

        request.json_parser = parse
        return request

    def cancel_open_orders(self, symbol, account_type, side=None, size=None):
        check_symbol(symbol)
        check_should_not_none(account_type, "account_type")
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type=account_type, subtype=symbol)
        builder = UrlParamsBuilder()
        builder.put_post("account-id", account.id)
        builder.put_post("symbol", symbol)
        builder.put_post("side", side)
        builder.put_post("size", size)
        request = self.__create_request_by_post_with_signature("/v1/order/orders/batchCancelOpenOrders", builder)

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            batch_cancel_result = BatchCancelResult()
            batch_cancel_result.success_count = data.get_int("success-count")
            batch_cancel_result.failed_count = data.get_int("failed-count")
            return batch_cancel_result

        request.json_parser = parse
        return request

    def cancel_client_order(self, client_order_id):
        check_should_not_none(client_order_id, "client-order-id")
        path = "/v1/order/orders/submitCancelClientOrder"
        builder = UrlParamsBuilder()
        builder.put_post("client-order-id", client_order_id)
        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    # 填充Order对象，应该在model中定义，因涉及api_key等，暂时放这里
    def format_order(self, json_data):
        account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                json_data.get_int("account-id")).account_type
        order = Order.json_parse(json_data, account_type)

        return order

    # 从json中解析订单对象的公共函数
    def get_order_json_parse(self, json_wrapper):
        data = json_wrapper.get_object("data")
        order = self.format_order(data)
        return order

    # 从json中解析订单对象列表的公共函数
    def get_order_list_json_parse(self, json_wrapper):
        order_list = list()
        data_array = json_wrapper.get_array("data")
        for item in data_array.get_items():
            order = self.format_order(item)
            order_list.append(order)
        return order_list

    def get_order(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/{}"
        path = path.format(order_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())
        request.json_parser = self.get_order_json_parse
        return request

    def get_order_by_client_order_id(self, client_order_id):
        check_should_not_none(client_order_id, "clientOrderId")
        path = "/v1/order/orders/getClientOrder"
        builder = UrlParamsBuilder()
        builder.put_url("clientOrderId", client_order_id)
        request = self.__create_request_by_get_with_signature(path, builder)
        request.json_parser = self.get_order_json_parse
        return request

    def get_match_results_by_order_id(self, order_id):
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/{}/matchresults"
        path = path.format(order_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            match_result_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                match_result = MatchResult()
                match_result.id = item.get_int("id")
                match_result.created_timestamp = item.get_int("created-at")
                match_result.filled_amount = item.get_float("filled-amount")
                match_result.filled_fees = item.get_float("filled-fees")
                match_result.match_id = item.get_int("match-id")
                match_result.order_id = item.get_int("order-id")
                match_result.price = item.get_float("price")
                match_result.source = item.get_string("source")
                match_result.symbol = item.get_string("symbol")
                match_result.order_type = item.get_string("type")
                match_result.role = item.get_string("role")
                match_result.filled_points = item.get_string("filled-points")
                match_result.fee_deduct_currency = item.get_string("fee-deduct-currency")
                match_result_list.append(match_result)
            return match_result_list

        request.json_parser = parse
        return request

    def get_match_results(self, symbol, order_type=None, start_date=None, end_date=None, size=None, from_id=None, direct=None):
        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        check_range(size, 1, 500, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("types", order_type)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        builder.put_url("direct", direct)
        request = self.__create_request_by_get_with_signature("/v1/order/matchresults", builder)

        def parse(json_wrapper):
            match_result_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                match_result = MatchResult()
                match_result.id = item.get_int("id")
                match_result.created_timestamp = item.get_int("created-at")
                match_result.filled_amount = item.get_float("filled-amount")
                match_result.filled_fees = item.get_float("filled-fees")
                match_result.match_id = item.get_int("match-id")
                match_result.order_id = item.get_int("order-id")
                match_result.price = item.get_float("price")
                match_result.source = item.get_string("source")
                match_result.symbol = item.get_string("symbol")
                match_result.order_type = item.get_string("type")
                match_result.role = item.get_string("role")
                match_result.filled_points = item.get_string("filled-points")
                match_result.fee_deduct_currency = item.get_string("fee-deduct-currency")
                match_result_list.append(match_result)
            return match_result_list

        request.json_parser = parse
        return request

    def withdraw(self, address, amount, currency, fee=None, address_tag=None):
        check_symbol(currency)
        check_should_not_none(address, "address")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("address", address)
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("fee", fee)
        builder.put_post("addr-tag", address_tag)

        request = self.__create_request_by_post_with_signature("/v1/dw/withdraw/api/create", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def cancel_withdraw(self, currency, withdraw_id):
        check_symbol(currency)
        check_should_not_none(withdraw_id, "withdraw_id")
        path = "/v1/dw/withdraw-virtual/{}/cancel"
        path = path.format(withdraw_id)
        request = self.__create_request_by_post_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def get_historical_orders(self, symbol, order_state, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None, start_time=None, end_time=None):
        check_symbol(symbol),
        check_should_not_none(order_state, "order_state")
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("types", order_type)
        builder.put_url("start-time", start_time)
        builder.put_url("end-time", end_time)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("from", start_id)
        builder.put_url("states", order_state)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/order/orders", builder)
        """
        def parse(json_wrapper):
            order_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                order = Order()
                order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                        item.get_int("account-id")).account_type
                order.amount = item.get_float("amount")
                order.canceled_timestamp = item.get_int_or_default("canceled-at", 0)
                order.finished_timestamp = item.get_int_or_default("finished-at", 0)
                order.order_id = item.get_int("id")
                order.symbol = item.get_string("symbol")
                order.price = item.get_float("price")
                order.created_timestamp = item.get_int("created-at")
                order.order_type = item.get_string("type")
                order.filled_amount = item.get_float("field-amount")
                order.filled_cash_amount = item.get_float("field-cash-amount")
                order.filled_fees = item.get_float("field-fees")
                order.source = item.get_string("source")
                order.state = item.get_string("state")
                order_list.append(order)
            return order_list
        """

        request.json_parser = self.get_order_list_json_parse
        return request

    def transfer_between_parent_and_sub(self, sub_uid, currency, amount, transfer_type):
        check_currency(currency)
        check_should_not_none(sub_uid, "sub_uid")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "transfer_type")
        builder = UrlParamsBuilder()
        builder.put_post("sub-uid", sub_uid)
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("type", transfer_type)
        request = self.__create_request_by_post_with_signature("/v1/subuser/transfer", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_current_user_aggregated_balance(self):
        request = self.__create_request_by_get_with_signature("/v1/subuser/aggregate-balance", UrlParamsBuilder())

        def parse(json_wrapper):
            balances = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                balance = Balance()
                balance.currency = item.get_string("currency")
                balance.type = item.get_string("type")
                balance.balance = item.get_float("balance")
                balances.append(balance)
            return balances

        request.json_parser = parse
        return request

    def get_specify_account_balance(self, sub_id):
        path = "/v1/account/accounts/{}"
        path = path.format(sub_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            complete_sub_account_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                complete_sub_account = CompleteSubAccountInfo()
                complete_sub_account.id = item.get_int("id")
                complete_sub_account.account_type = item.get_string("type")
                balances = list()
                data_array_in = item.get_array("list")
                for item_in in data_array_in.get_items():
                    balance = Balance()
                    balance.currency = item_in.get_string("currency")
                    balance.type = item_in.get_string("type")
                    balance.balance = item_in.get_float("balance")
                    balances.append(balance)
                complete_sub_account.balances = balances
                complete_sub_account_list.append(complete_sub_account)
            return complete_sub_account_list

        request.json_parser = parse
        return request

    def get_etf_candlestick(self, symbol, interval, size=None):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")
        check_should_not_none(interval, "interval")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("period", interval)
        builder.put_url("limit", size)
        request = self.__create_request_by_get("/quotation/market/history/kline", builder)

        def parse(json_wrapper):
            candlestick_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                candlestick = Candlestick()
                candlestick.open = item.get_float("open")
                candlestick.close = item.get_float("close")
                candlestick.low = item.get_float("low")
                candlestick.high = item.get_float("high")
                candlestick.amount = item.get_float("amount")
                candlestick.count = 0
                candlestick.volume = item.get_float("vol")
                candlestick_list.append(candlestick)
            return candlestick_list

        request.json_parser = parse
        return request

    def get_etf_swap_config(self, etf_symbol):
        check_symbol(etf_symbol)
        builder = UrlParamsBuilder()
        builder.put_url("etf_name", etf_symbol)
        request = self.__create_request_by_get("/etf/swap/config", builder)

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            etf_swap_config = EtfSwapConfig()
            etf_swap_config.purchase_max_amount = data.get_int("purchase_max_amount")
            etf_swap_config.purchase_min_amount = data.get_int("purchase_min_amount")
            etf_swap_config.redemption_max_amount = data.get_int("redemption_max_amount")
            etf_swap_config.redemption_min_amount = data.get_int("redemption_min_amount")
            etf_swap_config.purchase_fee_rate = data.get_float("purchase_fee_rate")
            etf_swap_config.redemption_fee_rate = data.get_float("redemption_fee_rate")
            etf_swap_config.status = data.get_string("etf_status")
            unit_price_data_array = data.get_array("unit_price")
            unit_price_list = list()
            for item in unit_price_data_array.get_items():
                unit_price = UnitPrice()
                unit_price.currency = item.get_string("currency")
                unit_price.amount = item.get_float("amount")
                unit_price_list.append(unit_price)
            etf_swap_config.unit_price_list = unit_price_list
            return etf_swap_config

        request.json_parser = parse
        return request

    def etf_swap(self, etf_symbol, amount, swap_type):
        check_symbol(etf_symbol)
        check_should_not_none(amount, "amount")
        check_should_not_none(swap_type, "swap_type")
        builder = UrlParamsBuilder()
        builder.put_post("etf_name", etf_symbol)
        builder.put_post("amount", amount)
        if swap_type == EtfSwapType.IN:
            request = self.__create_request_by_post_with_signature("/etf/swap/in", builder)
        else:
            request = self.__create_request_by_post_with_signature("/etf/swap/out", builder)

        def parse():
            return

        request.json_parser = parse
        return request

    def get_etf_swap_history(self, etf_symbol, offset, size):
        check_symbol(etf_symbol)
        check_range(size, 1, 100, "size")
        greater_or_equal(offset, 0, "offset")
        builder = UrlParamsBuilder()
        builder.put_url("etf_name", etf_symbol)
        builder.put_url("offset", offset)
        builder.put_url("limit", size)
        request = self.__create_request_by_get_with_signature("/etf/swap/list", builder)

        def parse(json_wrapper):
            etf_swap_history_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                etf_swap_history = EtfSwapHistory()
                etf_swap_history.created_timestamp = item.get_int("gmt_created")
                etf_swap_history.currency = item.get_string("currency")
                etf_swap_history.amount = item.get_float("amount")
                etf_swap_history.type = item.get_string("type")
                etf_swap_history.status = item.get_int("status")
                detail = item.get_object("detail")
                etf_swap_history.rate = detail.get_float("rate")
                etf_swap_history.fee = detail.get_float("fee")
                etf_swap_history.point_card_amount = detail.get_float("point_card_amount")
                used_currency_array = detail.get_array("used_currency_list")
                used_currency_list = list()
                for currency in used_currency_array.get_items():
                    unit_price = UnitPrice()
                    unit_price.amount = currency.get_float("amount")
                    unit_price.currency = currency.get_string("currency")
                    used_currency_list.append(unit_price)
                etf_swap_history.used_currency_list = used_currency_list
                obtain_currency_array = detail.get_array("obtain_currency_list")
                obtain_currency_list = list()
                for currency in obtain_currency_array.get_items():
                    unit_price = UnitPrice()
                    unit_price.amount = currency.get_float("amount")
                    unit_price.currency = currency.get_string("currency")
                    obtain_currency_list.append(unit_price)
                etf_swap_history.obtain_currency_list = obtain_currency_list
                etf_swap_history_list.append(etf_swap_history)
            return etf_swap_history_list

        request.json_parser = parse
        return request

    def get_margin_balance_detail(self, symbol, sub_uid):
        #check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("sub-uid", sub_uid)
        request = self.__create_request_by_get_with_signature("/v1/margin/accounts/balance", builder)

        def parse(json_wrapper):
            margin_balance_detail_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                margin_balance_detail = MarginBalanceDetail()
                margin_balance_detail.id = item_in_data.get_int("id")
                margin_balance_detail.type = item_in_data.get_string("type")
                margin_balance_detail.symbol = item_in_data.get_string("symbol")
                margin_balance_detail.state = item_in_data.get_string("state")
                margin_balance_detail.fl_price = item_in_data.get_float("fl-price")
                margin_balance_detail.fl_type = item_in_data.get_string("fl-type")
                margin_balance_detail.risk_rate = item_in_data.get_float("risk-rate")
                balance_list = list()
                list_array = item_in_data.get_array("list")
                for item_in_list in list_array.get_items():
                    balance = Balance()
                    balance.currency = item_in_list.get_string("currency")
                    balance.balance_type = item_in_list.get_string("type")
                    balance.balance = item_in_list.get_float("balance")
                    balance_list.append(balance)
                margin_balance_detail.sub_account_balance_list = balance_list
                margin_balance_detail_list.append(margin_balance_detail)
            return margin_balance_detail_list

        request.json_parser = parse
        return request

    def get_fee_rate(self, symbols):
        check_symbol(symbols)
        builder = UrlParamsBuilder()
        builder.put_url("symbols", symbols)
        request = self.__create_request_by_get_with_signature("/v1/fee/fee-rate/get", builder)

        def parse(json_wrapper):
            fee_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                fee_rate = FeeRate()
                fee_rate.symbol = item_in_data.get_string("symbol")
                fee_rate.maker_fee = item_in_data.get_string("maker-fee")
                fee_rate.taker_fee = item_in_data.get_string("taker-fee")
                fee_list.append(fee_rate)
            return fee_list


        request.json_parser = parse
        return request

    def get_margin_loan_info(self, symbols):
        check_symbol(symbols)
        builder = UrlParamsBuilder()
        builder.put_url("symbols", symbols)
        request = self.__create_request_by_get_with_signature("/v1/margin/loan-info", builder)

        def parse(json_wrapper):
            result_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                margin_loan = MarginLoanInfo.json_parse(item_in_data)
                result_list.append(margin_loan)
            return result_list


        request.json_parser = parse
        return request

    def get_cross_margin_loan_info(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get_with_signature("/v1/cross-margin/loan-info", builder)

        def parse(json_wrapper):
            result_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                margin_loan = CrossMarginLoanInfo.json_parse(item_in_data)
                result_list.append(margin_loan)
            return result_list


        request.json_parser = parse
        return request

    def get_reference_transact_fee_rate(self, symbols):
        builder = UrlParamsBuilder()
        check_symbol(symbol=symbols)
        builder.put_url("symbols", symbols)
        request = self.__create_request_by_get_with_signature("/v2/reference/transact-fee-rate", builder)

        def parse(json_wrapper):
            result_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                fee_rate = TransactFeeRate.json_parse(item_in_data)
                result_list.append(fee_rate)
            return result_list


        request.json_parser = parse
        return request

    def transfer_between_futures_and_pro(self, currency, amount, transfer_type):
        check_currency(currency)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "transfer_type")
        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("type", transfer_type)
        request = self.__create_request_by_post_with_signature("/v1/futures/transfer", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")  # transfer ID

        request.json_parser = parse
        return request

    def get_order_in_recent_48hour(self, symbol, start_time, end_time, size, direct):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("start-time", start_time)
        builder.put_url("end-time", end_time)
        builder.put_url("size", size)
        builder.put_url("direct", direct)
        request = self.__create_request_by_get_with_signature("/v1/order/history", builder)

        request.json_parser = self.get_order_list_json_parse
        return request

    def get_reference_currencies(self, currency, is_authorized_user):
        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("authorizedUser", is_authorized_user)
        request = self.__create_request_by_get("/v2/reference/currencies", builder)

        def parse(json_wrapper):
            reference_currency_list = []

            data_array = json_wrapper.get_array("data")
            for reference_currency_data in data_array.get_items():
                reference_currency = ReferenceCurrency()
                reference_currency.currency = reference_currency_data.get_string("currency")
                reference_currency.instStatus = reference_currency_data.get_string("instStatus")
                chains_array = reference_currency_data.get_array("chains")
                for chain_in_data in chains_array.get_items():
                    chain_obj = Chain()

                    chain_obj.chain = chain_in_data.get_string("chain")
                    chain_obj.baseChain = chain_in_data.get_string_or_default("baseChain", "")
                    chain_obj.baseChainProtocol = chain_in_data.get_string_or_default("baseChainProtocol", "")
                    chain_obj.numOfConfirmations = chain_in_data.get_float("numOfConfirmations")
                    chain_obj.numOfFastConfirmations = chain_in_data.get_float("numOfFastConfirmations")

                    chain_obj.depositStatus = chain_in_data.get_string("depositStatus")
                    chain_obj.minDepositAmt = chain_in_data.get_float("minDepositAmt")
                    chain_obj.withdrawStatus = chain_in_data.get_string("withdrawStatus")
                    chain_obj.minWithdrawAmt = chain_in_data.get_float("minWithdrawAmt")
                    chain_obj.maxWithdrawAmt = chain_in_data.get_float("maxWithdrawAmt")
                    chain_obj.withdrawQuotaPerDay = chain_in_data.get_float("withdrawQuotaPerDay")
                    chain_obj.withdrawQuotaPerYear = chain_in_data.get_float("withdrawQuotaPerYear")
                    chain_obj.withdrawQuotaTotal = chain_in_data.get_float("withdrawQuotaTotal")
                    chain_obj.withdrawFeeType = chain_in_data.get_string("withdrawFeeType")
                    chain_obj.transactFeeWithdraw = chain_in_data.get_float_or_default("transactFeeWithdraw", 0)
                    chain_obj.minTransactFeeWithdraw = chain_in_data.get_float_or_default("minTransactFeeWithdraw", 0)
                    chain_obj.maxTransactFeeWithdraw = chain_in_data.get_float_or_default("maxTransactFeeWithdraw", 0)
                    chain_obj.transactFeeRateWithdraw = chain_in_data.get_float_or_default("transactFeeRateWithdraw", 0)
                    reference_currency.chains.append(chain_obj)
                reference_currency_list.append(reference_currency)
            return reference_currency_list

        request.json_parser = parse
        return request

    def get_deposit_withdraw(self, op_type, currency, from_id, size, direct):
        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("type", op_type)
        builder.put_url("from", from_id)
        builder.put_url("direct", direct)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/v1/query/deposit-withdraw", builder)

        def parse_deposit(json_wrapper):
            deposit = Deposit()
            deposit.id = json_wrapper.get_int("id")
            deposit.currency = json_wrapper.get_string("currency")
            deposit.tx_hash = json_wrapper.get_string("tx-hash")
            deposit.amount = json_wrapper.get_float("amount")
            deposit.address = json_wrapper.get_string("address")
            deposit.address_tag = json_wrapper.get_string("address-tag")
            deposit.fee = json_wrapper.get_float("fee")
            deposit.type = json_wrapper.get_string("type")
            deposit.chain = json_wrapper.get_string("chain")
            deposit.created_timestamp = json_wrapper.get_int("created-at")
            deposit.updated_timestamp = json_wrapper.get_int("updated-at")
            deposit.deposit_state = json_wrapper.get_string("state")
            return deposit

        def parse_withdraw(json_wrapper):
            withdraw = Withdraw()
            withdraw.id = json_wrapper.get_int("id")
            withdraw.currency = json_wrapper.get_string("currency")
            withdraw.tx_hash = json_wrapper.get_string("tx-hash")
            withdraw.amount = json_wrapper.get_float("amount")
            withdraw.address = json_wrapper.get_string("address")
            withdraw.address_tag = json_wrapper.get_string("address-tag")
            withdraw.fee = json_wrapper.get_float("fee")
            withdraw.type = json_wrapper.get_string("type")
            withdraw.chain = json_wrapper.get_string("chain")
            withdraw.created_timestamp = json_wrapper.get_int("created-at")
            withdraw.updated_timestamp = json_wrapper.get_int("updated-at")
            withdraw.withdraw_state = json_wrapper.get_string("state")
            return withdraw

        def parse(json_wrapper):
            ret_list = []
            if op_type == DepositWithdraw.DEPOSIT:
                data_array = json_wrapper.get_array("data")
                for deposit_data in data_array.get_items():
                    deposit = parse_deposit(deposit_data)
                    ret_list.append(deposit)
            elif op_type == DepositWithdraw.WITHDRAW:
                data_array = json_wrapper.get_array("data")
                for withdraw_data in data_array.get_items():
                    withdraw = parse_withdraw(withdraw_data)
                    ret_list.append(withdraw)

            return ret_list
        request.json_parser = parse
        return request


    def get_account_deposit_address(self, currency):
        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        request = self.__create_request_by_get_with_signature("/v2/account/deposit/address", builder)

        def parse(json_wrapper):
            ret_list = []
            data_array = json_wrapper.get_array("data")
            for address_data in data_array.get_items():
                obj = ChainDepositAddress()
                obj.currency = address_data.get_string("currency")
                obj.address = address_data.get_string("address")
                obj.addressTag = address_data.get_string("addressTag")
                obj.chain = address_data.get_string("chain")
                ret_list.append(obj)
            return ret_list

        request.json_parser = parse
        return request

    def get_sub_user_deposit_address(self, sub_uid, currency):
        builder = UrlParamsBuilder()
        builder.put_url("subUid", sub_uid)
        builder.put_url("currency", currency)
        request = self.__create_request_by_get_with_signature("/v2/sub-user/deposit-address", builder)

        def parse(json_wrapper):
            ret_list = []
            data_array = json_wrapper.get_array("data")
            for address_data in data_array.get_items():
                obj = ChainDepositAddress()
                obj.currency = address_data.get_string("currency")
                obj.address = address_data.get_string("address")
                obj.addressTag = address_data.get_string("addressTag")
                obj.chain = address_data.get_string("chain")
                ret_list.append(obj)
            return ret_list

        request.json_parser = parse
        return request

    def get_account_withdraw_quota(self, currency):
        check_should_not_none(currency, "currency")
        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        request = self.__create_request_by_get_with_signature("/v2/account/withdraw/quota", builder)

        def parse(json_wrapper):
            ret_list = []
            data = json_wrapper.get_object("data")
            chains_info = data.get_array("chains")
            for chain_data in chains_info.get_items():
                obj = WithdrawQuota()
                obj.chain = chain_data.get_string("chain")
                obj.maxWithdrawAmt = chain_data.get_string("maxWithdrawAmt")
                obj.withdrawQuotaPerDay = chain_data.get_string("withdrawQuotaPerDay")
                obj.remainWithdrawQuotaPerDay = chain_data.get_string("remainWithdrawQuotaPerDay")
                obj.withdrawQuotaPerYear = chain_data.get_string("withdrawQuotaPerYear")
                obj.remainWithdrawQuotaPerYear = chain_data.get_string("remainWithdrawQuotaPerYear")
                obj.withdrawQuotaTotal = chain_data.get_string("withdrawQuotaTotal")
                obj.remainWithdrawQuotaTotal = chain_data.get_string("remainWithdrawQuotaTotal")

                ret_list.append(obj)
            return ret_list

        request.json_parser = parse
        return request

    def post_create_withdraw(self, address, amount, currency, fee, chain, address_tag):
        check_should_not_none(address, "address")
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        check_should_not_none(fee, "fee")
        builder = UrlParamsBuilder()
        builder.put_post("address", address)
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("fee", fee)
        builder.put_post("chain", chain)
        builder.put_post("addr-tag", address_tag)

        request = self.__create_request_by_post_with_signature("/v1/dw/withdraw/api/create", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int_or_default("data", 0)

        request.json_parser = parse
        return request

    def post_cancel_withdraw(self, withdraw_id):
        check_should_not_none(withdraw_id, "withdraw-id")
        path = "/v1/dw/withdraw-virtual/{}/cancel"
        path = path.format(withdraw_id)

        request = self.__create_request_by_post_with_signature(path, UrlParamsBuilder())
        def parse(json_wrapper):
            return json_wrapper.get_int_or_default("data", 0)

        request.json_parser = parse
        return request

    def post_cross_margin_transfer_in(self, currency, amount):
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        path = "/v1/cross-margin/transfer-in"

        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)

        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return json_wrapper.get_int_or_default("data", 0)

        request.json_parser = parse
        return request

    def post_cross_margin_transfer_out(self, currency, amount):
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        path = "/v1/cross-margin/transfer-out"

        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)

        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return json_wrapper.get_int_or_default("data", 0)

        request.json_parser = parse
        return request

    def post_cross_margin_create_loan_orders(self, currency, amount):
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        path = "/v1/cross-margin/orders"

        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)

        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return json_wrapper.get_int_or_default("data", 0)

        request.json_parser = parse
        return request

    def post_cross_margin_loan_order_repay(self, order_id, amount):
        check_should_not_none(order_id, "order-id")
        check_should_not_none(amount, "amount")
        path = "/v1/cross-margin/orders/{order_id}/repay".format(order_id=order_id)

        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)

        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def get_cross_margin_loan_orders(self, currency, state, start_date, end_date, from_id, size, direct, sub_uid):

        path = "/v1/cross-margin/loan-orders"
        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("state", state)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        builder.put_url("direct", direct)
        builder.put_url("sub-uid", sub_uid)

        request = self.__create_request_by_get_with_signature(path, builder)

        def parse(json_wrapper):
            ret_list = []
            order_list = json_wrapper.get_array("data")
            for order_data in order_list.get_items():
                obj = LoanOrder()
                obj.id = order_data.get_int("id")
                obj.user_id = order_data.get_int("user-id")
                obj.account_id = order_data.get_int("account-id")
                obj.currency = order_data.get_string("currency")
                obj.load_amount = order_data.get_float("loan-amount")
                obj.loan_balance = order_data.get_float("loan-balance")
                obj.interest_amount = order_data.get_float("interest-amount")
                obj.interest_balance = order_data.get_float("interest-balance")
                obj.filled_points = order_data.get_float("filled-points")
                obj.filled_ht = order_data.get_float("filled-ht")
                obj.created_at = order_data.get_int("created-at")
                obj.accrued_at = order_data.get_int("accrued-at")
                obj.state = order_data.get_string("state")

                ret_list.append(obj)
            return ret_list

        request.json_parser = parse
        return request

    def get_cross_margin_account_balance(self, sub_uid):

        path = "/v1/cross-margin/accounts/balance"
        builder = UrlParamsBuilder()
        builder.put_url("sub-uid", sub_uid)



        request = self.__create_request_by_get_with_signature(path, builder)

        def parse(json_wrapper):
            account_balance = CrossMarginAccountBalance()
            data_obj = json_wrapper.get_object("data")
            account_balance.id = data_obj.get_int("id")
            account_balance.type = data_obj.get_string("type")
            account_balance.state = data_obj.get_string("state")
            account_balance.risk_rate = data_obj.get_int("risk-rate")
            account_balance.acct_balance_sum = data_obj.get_float("acct-balance-sum")
            account_balance.debt_balance_sum = data_obj.get_float("debt-balance-sum")
            balance_list = data_obj.get_array("list")
            for balance_data in balance_list.get_items():
                balance_obj = Balance()
                balance_obj.currency = balance_data.get_string("currency")
                balance_obj.balance_type = balance_data.get_string("type")
                balance_obj.balance = balance_data.get_float("balance")
                account_balance.list.append(balance_obj)

            return account_balance

        request.json_parser = parse
        return request

    def get_account_history(self, account_id, currency,
                                transact_types, start_time, end_time,
                                sort, size):
        path = "/v1/account/history"

        builder = UrlParamsBuilder()
        builder.put_url("account-id", account_id)
        builder.put_url("currency", currency)
        builder.put_url("transact-types", transact_types)
        builder.put_url("start-time", start_time)
        builder.put_url("end-time", end_time)
        builder.put_url("sort", sort)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature(path, builder)

        def parse(json_wrapper):
            account_history_list = []
            data_obj = json_wrapper.get_array("data")
            for history_data in data_obj.get_items():
                account_history = AccountHistory()
                account_history.account_id = history_data.get_int("account-id")
                account_history.currency = history_data.get_string("currency")
                account_history.transact_amt = history_data.get_string("transact-amt")
                account_history.transact_type = history_data.get_string("transact-type")
                account_history.avail_balance = history_data.get_string("avail-balance")
                account_history.acct_balance = history_data.get_string("acct-balance")
                account_history.record_id = history_data.get_string("record-id")
                account_history.transact_time = history_data.get_int("transact-time")
                account_history_list.append(account_history)

            return account_history_list

        request.json_parser = parse
        return request

    def sub_user_management(self, sub_uid, action):
        check_should_not_none(sub_uid, "sub_uid")
        check_should_not_none(action, "action")
        builder = UrlParamsBuilder()
        builder.put_post("subUid", sub_uid)
        builder.put_post("action", action)
        request = self.__create_request_by_post_with_signature("/v2/sub-user/management", builder)

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            return SubUidManagement.json_parse(data)

        request.json_parser = parse
        return request

    def get_market_tickers(self):
        request = self.__create_request_by_get_with_signature("/market/tickers", UrlParamsBuilder())

        def parse(json_wrapper):
            result_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                market_ticker = MarketTicker.json_parse(item_in_data)
                result_list.append(market_ticker)
            return result_list

        request.json_parser = parse
        return request

    def get_account_ledger(self, account_id, currency, transact_types, start_time, end_time, sort, limit, from_id):
        builder = UrlParamsBuilder()
        builder.put_url("accountId", account_id)
        builder.put_url("currency", currency)
        builder.put_url("transactTypes", transact_types)
        builder.put_url("startTime", start_time)
        builder.put_url("endTime", end_time)
        builder.put_url("sort", sort)
        builder.put_url("limit", limit)
        builder.put_url("fromId", from_id)
        request = self.__create_request_by_get_with_signature("/v2/account/ledger", builder)

        def parse(json_wrapper):
            result_list = list()
            data_array = json_wrapper.get_array("data")
            for item_in_data in data_array.get_items():
                account_ledger = AccountLedger.json_parse(item_in_data)
                result_list.append(account_ledger)
            return result_list

        request.json_parser = parse
        return request

    def get_system_status(self):
        request = RestApiRequest()
        request.method = "GET"
        request.host = "https://status.huobigroup.com"
        request.header.update({'Content-Type': 'application/json'})
        request.url = "/api/v2/summary.json"
        return request
