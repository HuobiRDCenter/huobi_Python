from huobi.exception.huobiapiexception import HuobiApiException
from huobi.impl.restapiinvoker import call_sync
from huobi.model.user import User


class AccountInfoMap:

    user_map = dict()

    def update_user_info(self, api_key, request_impl):
        accounts = call_sync(request_impl.get_accounts())
        user = User()
        user.accounts = accounts
        self.user_map[api_key] = user

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


account_info_map = AccountInfoMap()
