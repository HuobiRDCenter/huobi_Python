from huobi.constant import *
from huobi.model.account import *
from huobi.utils import *
import aiohttp
import asyncio
from huobi.utils.input_checker import check_in_list


class AccountClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: Init logger, default is False, True will init logger handler
        """
        self.__kwargs = kwargs

    # 账户信息
    def get_accounts(self):
        from huobi.service.account.get_accounts import GetAccountsService
        return GetAccountsService({}).request(**self.__kwargs)

    # 账户余额
    def get_balance(self, account_id: 'int'):
        check_should_not_none(account_id, "account-id")
        params = {
            "account-id": account_id
        }
        from huobi.service.account.get_balance import GetBalanceService
        return GetBalanceService(params).request(**self.__kwargs)

    def get_account_by_type_and_symbol(self, account_type, symbol):
        accounts = self.get_accounts()
        if accounts and len(accounts):
            for account_obj in accounts:
                if account_obj.type == account_type:
                    if account_type == AccountType.MARGIN:
                        if symbol == account_obj.subtype:
                            return account_obj
                    else:
                        return account_obj
        return None

    async def async_get_account_balance(self, balance_full_url, account_id, ret_map):
        async with aiohttp.ClientSession() as session:
            async with session.get(balance_full_url) as resp:
                json = await resp.json()
                ret_map[account_id] = json
                return json

    """
    (SDK encapsulated api) to easily use but not recommend for low performance and frequence limitation
    """

    def get_account_balance(self) -> list:
        from huobi.service.account.get_balance import GetBalanceService
        """
        Get the balance of a all accounts.

        :return: The information of all account balance.
        """
        server_url = get_default_server_url(self.__kwargs.get("url"))
        tasks = []
        account_obj_map = {}
        accounts = self.get_accounts()
        account_balance_list = []
        account_balance_json_map = {}
        for account_item in accounts:
            account_obj_map[account_item.id] = account_item
            balance_params = {"account-id": account_item.id}
            balance_request = GetBalanceService(balance_params).get_request(**self.__kwargs)
            balance_url = server_url + balance_request.url
            tasks.append(asyncio.ensure_future(
                self.async_get_account_balance(balance_url, account_item.id, account_balance_json_map)))

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as ee:
            print(ee)
        finally:
            # loop.close()  #for thread safe, the event loop can't be closed
            pass

        for account_id, account_balance_json in account_balance_json_map.items():
            account_balance = AccountBalance.json_parse(account_balance_json.get("data", {}))
            account_obj_tmp = account_obj_map.get(account_id, None)
            account_balance.subtype = None if account_obj_tmp is None else account_obj_tmp.subtype
            account_balance_list.append(account_balance)

        del account_balance_json_map
        del tasks
        return account_balance_list

    def sub_account_update(self, mode: 'AccountBalanceMode', callback, error_handler=None):
        """
        Subscribe accounts update

        :param mode: subscribe mode
                "0" : for balance
                "1" : for available and balance
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event: 'PriceDepthEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass

        :return:  No return
        """

        check_should_not_none(callback, "callback")
        if str(mode) == AccountBalanceMode.TOTAL:
            mode = AccountBalanceMode.TOTAL
        else:
            mode = AccountBalanceMode.BALANCE

        params = {
            "mode": mode,
        }

        from huobi.service.account.sub_account_update_v2 import SubAccountUpdateV2Service
        SubAccountUpdateV2Service(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_account_balance(self, callback, client_req_id=None, error_handler=None):
        """
        Subscribe account changing event. If the balance is updated, server will send the data to client and onReceive in callback will be called.

        :param client_req_id: client request ID
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(account_event: 'AccountEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """

        check_should_not_none(callback, "callback")
        params = {
            "client_req_id": client_req_id
        }

        from huobi.service.account.req_account_balance import ReqAccountBalanceService
        ReqAccountBalanceService(params).subscribe(callback, error_handler, **self.__kwargs)

    # 币币现货账户与合约账户划转
    def transfer_between_futures_and_pro(self, currency: 'str', amount: 'float',
                                         transfer_type: 'TransferFuturesPro') -> int:
        """
        Transfer Asset between Futures and Contract.

        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, need be "futures-to-pro" or "pro-to-futures" (mandatory)
        :return: The order id.
        """

        check_currency(currency)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "transfer_type")
        params = {
            "currency": currency,
            "amount": amount,
            "type": transfer_type
        }

        from huobi.service.account.post_futures_and_pro_transfer import PostTransferBetweenFuturesAndProService
        return PostTransferBetweenFuturesAndProService(params).request(**self.__kwargs)

    # 账户流水
    def get_account_history(self, account_id: 'int', currency: 'str' = None,
                            transact_types: 'str' = None, start_time: 'int' = None, end_time: 'int' = None,
                            sort: 'str' = None, size: 'int' = None, from_id: 'int' = None):
        """
        get account change record
        :param account_id: account id (mandatory)
        :param currency: currency as "btc,eth" (optional)
        :param transact_types: see AccountTransactType, the value can be "trade" (交易),"etf"（ETF申购）, "transact-fee"（交易手续费）, "deduction"（手续费抵扣）, "transfer"（划转）, "credit"（借币）, "liquidation"（清仓）, "interest"（币息）, "deposit"（充币），"withdraw"（提币）, "withdraw-fee"（提币手续费）, "exchange"（兑换）, "other-types"（其他） (optional)
        :param start_time&end_time: for time range to search (optional)
        :param sort: see SortDesc, "asc" or "desc" (optional)
        :param size: page size (optional)
        :param from_id: First record ID in this query (only valid for next page querying, see Note 2)(optional)
        :return: account change record list.
        """
        check_should_not_none(account_id, "account-id")
        params = {
            "account-id": account_id,
            "currency": currency,
            "transact-types": transact_types,
            "start-time": start_time,
            "end-time": end_time,
            "sort": sort,
            "size": size,
            "from-id": from_id
        }
        from huobi.service.account.get_account_history import GetAccountHistoryService
        return GetAccountHistoryService(params).request(**self.__kwargs)

    # 财务流水
    def get_account_ledger(self, account_id: 'int', currency: 'str' = None, transact_types: 'str' = None,
                           start_time: 'int' = None, end_time: 'int' = None, sort: 'str' = None, limit: 'int' = None,
                           from_id: 'int' = None) -> list:
        """
        get account ledger
        :param account_id: account id (mandatory)
        :param currency: currency as "btc,eth" (optional)
        :param transact_types: see AccountTransactType, the value can be "trade" (交易),"etf"（ETF申购）, "transact-fee"（交易手续费）, "deduction"（手续费抵扣）, "transfer"（划转）, "credit"（借币）, "liquidation"（清仓）, "interest"（币息）, "deposit"（充币），"withdraw"（提币）, "withdraw-fee"（提币手续费）, "exchange"（兑换）, "other-types"（其他） (optional)
        :param start_time&end_time: for time range to search (optional)
        :param sort: see SortDesc, "asc" or "desc" (optional)
        :return: account ledger list.
        """

        check_should_not_none(account_id, "accountId")

        params = {
            "accountId": account_id,
            "currency": currency,
            "transactTypes": transact_types,
            "startTime": start_time,
            "endTime": end_time,
            "sort": sort,
            "limit": limit,
            "fromId": from_id
        }
        from huobi.service.account.get_account_ledger import GetAccountLedgerService
        return GetAccountLedgerService(params).request(**self.__kwargs)

    # 资产划转
    def post_account_transfer(self, from_user: 'int', from_account_type: 'str', from_account: 'int', to_user: 'int',
                              to_account_type: 'str', to_account: 'int', currency: 'str', amount: 'str'):
        check_should_not_none(from_user, "from-user")
        check_should_not_none(from_account_type, "from-account-type")
        check_should_not_none(from_account, "from_account")
        check_should_not_none(to_user, "to-user")
        check_should_not_none(to_account, "to-account")
        check_should_not_none(to_account_type, "to-account")
        check_should_not_none(currency, "currency")

        check_in_list(from_account_type, [AccountType.SPOT], "from_account_type")
        check_in_list(to_account_type, [AccountType.SPOT], "to_account_type")

        params = {
            "from-user": from_user,
            "from-account-type": from_account_type,
            "from-account": from_account,
            "to-user": to_user,
            "to-account-type": to_account_type,
            "to-account": to_account,
            "currency": currency,
            "amount": amount
        }
        from huobi.service.account.post_account_transfer import PostAccountTransferService
        return PostAccountTransferService(params).request(**self.__kwargs)

    # 获取指定账户资产估值（现货、杠杆、OTC）
    def get_account_asset_valuation(self, account_type, valuation_currency: 'str' = None, sub_uid: 'int' = None):
        check_should_not_none(account_type, "account-type")

        params = {
            "accountType": account_type,
            "valuationCurrency": valuation_currency.upper(),
            "subUid": sub_uid
        }
        from huobi.service.account.get_account_asset_valuation import GetAccountAssetValuationService
        return GetAccountAssetValuationService(params).request(**self.__kwargs)

    # 点卡余额查询
    def get_account_point(self, sub_uid: 'str' = None):
        params = {
            "subUid": sub_uid
        }

        from huobi.service.account.get_account_point import GetAccountPointService
        return GetAccountPointService(params).request(**self.__kwargs)

    # 点卡划转
    def post_point_transfer(self, from_uid: 'str', to_uid: 'str', group_id: 'str', amount: 'str'):

        params = {
            "fromUid": from_uid,
            "toUid": to_uid,
            "groupId": group_id,
            "amount": amount
        }

        from huobi.service.account.post_point_transfer import PostPointTransferService
        return PostPointTransferService(params).request(**self.__kwargs)

    # 获取平台资产总估值
    def get_account_valuation(self, account_type: 'str' = None, valuation_currency: 'str' = None):

        params = {
            "accountType": account_type,
            "valuationCurrency": valuation_currency
        }

        from huobi.service.account.get_account_valuation import GetAccountValuationService
        return GetAccountValuationService(params).request(**self.__kwargs)

    # 【通用】现货-合约账户和OTC账户间进行资金的划转
    def get_account_transfer(self, from_: 'str', to: 'str', currency: 'str', amount: 'float', margin_account: 'str'):

        params = {
            "from": from_,
            "to": to,
            "currency": currency,
            "amount": amount,
            "margin-account": margin_account
        }

        from huobi.service.account.get_account_transfer import GetAccountTransferService
        return GetAccountTransferService(params).request(**self.__kwargs)

    # 用户抵扣信息查询
    def get_user_info(self):
        params = {}
        from huobi.service.account.get_user_info import GetAccountUserInfoService
        return GetAccountUserInfoService(params).request(**self.__kwargs)

    # 可抵扣币种查询信息
    def get_overview_info(self):
        params = {}
        from huobi.service.account.get_overview_info import GetAccountOverviewInfoService
        return GetAccountOverviewInfoService(params).request(**self.__kwargs)

    # 点卡划转
    def post_fee_switch(self, switch_type: 'int', deduction_currency: 'str'):
        check_should_not_none(switch_type, "switchType")
        params = {
            "switchType": switch_type,
            "deductionCurrency": deduction_currency
        }

        from huobi.service.account.post_fee_switch import PostFeeSwitchService
        return PostFeeSwitchService(params).request(**self.__kwargs)
