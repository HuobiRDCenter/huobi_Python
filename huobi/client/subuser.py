from huobi.utils import *
from huobi.constant import *
from huobi.utils.input_checker import check_in_list


class SubuserClient(object):
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

    def post_create_subuser(self, user_list):
        check_should_not_none(user_list, 'userList')

        params = user_list
        from huobi.service.subuser.post_create_subuser import PostSubuserCreationService
        return PostSubuserCreationService(params).request(**self.__kwargs)

    def post_set_tradable_market(self, sub_uids, account_type: 'SubuserTradePrivilegeType',
                                 activation: 'SubUserTradeStatus'):
        check_should_not_none(sub_uids, 'subUids')
        check_should_not_none(account_type, 'accountType')
        check_should_not_none(activation, 'activation')

        check_in_list(account_type,
                      [SubuserTradePrivilegeType.MARGIN, SubuserTradePrivilegeType.SUPER_MARGIN], "accountType")
        check_in_list(activation, [SubUserTradeStatus.ACTIVATED, SubUserTradeStatus.DEACTIVATED], "activation")

        params = {
            'subUids': sub_uids,
            'accountType': account_type,
            'activation': activation
        }
        from huobi.service.subuser.post_tradable_market import PostTradableMarketService
        return PostTradableMarketService(params).request(**self.__kwargs)

    def post_set_subuser_transferability(self, sub_uids: 'str', transferrable: 'bool',
                                         account_type: 'AccountType' = AccountType.SPOT):
        check_should_not_none(sub_uids, 'subUids')
        check_should_not_none(transferrable, 'transferrable')
        check_in_list(account_type, [AccountType.SPOT], 'accountType')

        params = {
            "subUids": sub_uids,
            "accountType": account_type,
            "transferrable": transferrable
        }
        from huobi.service.subuser.post_set_transferability import PostSetSubuserTransferability
        return PostSetSubuserTransferability(params).request(**self.__kwargs)

    def post_subuser_apikey_generate(self, otp_token: 'str', sub_uid: 'int', note: 'str', permission: 'bool',
                                     ip_addresses: 'str' = None):
        check_should_not_none(otp_token, 'otpToken')
        check_should_not_none(sub_uid, 'subUid')
        check_should_not_none(note, 'note')
        check_should_not_none(permission, 'permission')
        # check_in_list(permission, [AccountType.SPOT], 'accountType')

        params = {
            "otpToken": otp_token,
            "subUid": sub_uid,
            "note": note,
            "permission": permission,
            "ipAddresses": ip_addresses
        }
        from huobi.service.subuser.post_subuser_apikey_generation import PostSubuserApikeyGenerationService
        return PostSubuserApikeyGenerationService(params).request(**self.__kwargs)

    def get_user_apikey_info(self, uid: 'str', access_key: 'str' = None):
        check_should_not_none(uid, 'uid')

        params = {
            "uid": uid,
            "accessKey": access_key
        }
        from huobi.service.subuser.get_user_apikey_info import GetUserApikeyInfoService
        return GetUserApikeyInfoService(params).request(**self.__kwargs)

    def post_subuser_apikey_modification(self, sub_uid: 'str', access_key: 'str', note: 'str' = None,
                                         permission: 'str' = None, ip_addresses: 'str' = None):
        check_should_not_none(sub_uid, 'subUid')
        check_should_not_none(access_key, 'accessKey')

        params = {
            "subUid": sub_uid,
            "accessKey": access_key,
            "note": note,
            "permission": permission,
            "ipAddresses": ip_addresses
        }
        from huobi.service.subuser.post_subuser_apikey_modification import PostSubuserApikeyModificationService
        return PostSubuserApikeyModificationService(params).request(**self.__kwargs)

    def post_subuser_apikey_deletion(self, sub_uid: 'str', access_key: 'str'):
        check_should_not_none(sub_uid, 'subUid')
        check_should_not_none(access_key, 'accessKey')

        params = {
            "subUid": sub_uid,
            "accessKey": access_key
        }
        from huobi.service.subuser.post_subuser_apikey_deletion import PostSubuserApikeyDeletionService
        return PostSubuserApikeyDeletionService(params).request(**self.__kwargs)

    def get_uid(self):
        params = {
        }
        from huobi.service.subuser.get_uid import GetUidService
        return GetUidService(params).request(**self.__kwargs)
