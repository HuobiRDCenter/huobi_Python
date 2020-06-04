import asyncio
import time

from huobi.client.account import AccountClient, AccountBalance, get_default_server_url, AccountType


class AccountClientPerformance(AccountClient):

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
        self.__kwargs["performance_test"] = True
        super(AccountClientPerformance, self).__init__(**self.__kwargs)

    def get_account_balance(self) -> list:
        from huobi.service.account.get_balance import GetBalanceService
        """
        Get the balance of a all accounts.

        :return: The information of all account balance.
        """
        server_url = get_default_server_url(self.__kwargs.get("url"))
        tasks = []
        accounts, req_cost_1, cost_manual_1  = super(AccountClientPerformance, self).get_accounts()
        start_time = time.time()
        account_balance_list = []
        account_balance_json_map = {}
        for account_item in accounts:
            balance_params = {"account-id": account_item.id}
            balance_request = GetBalanceService(balance_params).get_request(**self.__kwargs)
            balance_url = server_url + balance_request.url
            tasks.append(asyncio.ensure_future(
                super(AccountClientPerformance, self).async_get_account_balance(balance_url, account_item.id, account_balance_json_map)))

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
            account_balance_list.append(account_balance)

        del account_balance_json_map
        del tasks
        end_time = time.time()
        async_balane_cost = round(end_time - start_time, 6)
        return account_balance_list, req_cost_1 + async_balane_cost, cost_manual_1 + async_balane_cost

    def get_account_by_type_and_symbol(self, account_type, symbol):
        accounts, req_cost, cost_manual = super(AccountClientPerformance, self).get_accounts()
        if accounts and len(accounts):
            for account_obj in accounts:
                if account_obj.type == account_type:
                    if account_type == AccountType.MARGIN:
                        if symbol == account_obj.subtype:
                            return account_obj, req_cost, cost_manual
                    else:
                        return account_obj, req_cost, cost_manual

        return None, req_cost, cost_manual
