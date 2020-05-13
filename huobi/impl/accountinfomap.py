from huobi.exception.huobiapiexception import HuobiApiException
from huobi.impl.restapiinvoker import call_sync
from huobi.model.user import User


class AccountInfoMap:

    user_map = dict()
    account_id_type_map = dict()
    account_type_id_map = dict()

    def update_user_info(self, api_key, request_impl):
        accounts = call_sync(request_impl.get_accounts())
        user = User()
        user.accounts = accounts
        self.user_map[api_key] = user
        if accounts and len(accounts):
            self.account_id_type_map[api_key] = {}
            self.account_type_id_map[api_key] = {}
            for account_item in accounts:
                self.account_id_type_map[api_key][account_item.id] = account_item.account_type
                self.account_type_id_map[api_key][account_item.account_type] = account_item.id

    def get_user(self, api_key):
        if api_key is None or api_key == "":
            raise HuobiApiException(HuobiApiException.KEY_MISSING, "[User] Key is empty or null")
        if api_key not in self.user_map:
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[User] Cannot found user by key: " + api_key)
        return self.user_map[api_key]

    def get_account_by_id(self, api_key, account_id):
        user = self.get_user(api_key)
        account = user.get_account_by_id(account_id)
        if account is None:
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR,
                                    "[User] Cannot find the account, key: " +
                                    api_key + ", account id: " + str(account_id))
        return account

    def get_all_accounts(self, api_key):
        user = self.get_user(api_key)
        return user.accounts

    def get_account_type_by_id(self, api_key, account_id):
        if api_key is None or api_key == "":
            raise HuobiApiException(HuobiApiException.KEY_MISSING, "[User] Key is empty or null")
        if api_key not in self.account_id_type_map:
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[User] Cannot found account_id by key: " + api_key)
        return self.account_id_type_map.get(api_key, {}).get(account_id, None)

    def get_account_id_by_type(self, api_key, account_type):
        if api_key is None or api_key == "":
            raise HuobiApiException(HuobiApiException.KEY_MISSING, "[User] Key is empty or null")
        if api_key not in self.account_type_id_map:
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[User] Cannot found account_type by key: " + api_key)
        return self.account_type_id_map.get(api_key, {}).get(account_type, None)

    def get_all_accounts_without_check(self, api_key):
        if api_key is None or api_key == "":
            raise HuobiApiException(HuobiApiException.KEY_MISSING, "[User] Key is empty or null")

        user = self.user_map.get(api_key, None)
        return None if (user is None) else user.accounts

account_info_map = AccountInfoMap()
