from huobi.model.wallet import DepositHistory
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

    # 子用户创建
    def post_create_subuser(self, user_list):
        check_should_not_none(user_list, 'userList')

        params = user_list
        from huobi.service.subuser.post_create_subuser import PostSubuserCreationService
        return PostSubuserCreationService(params).request(**self.__kwargs)

    # 设置子用户交易权限
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

    # 设置子用户资产转出权限
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

    # 子用户APIkey创建
    def post_subuser_apikey_generate(self, otp_token: 'str', sub_uid: 'int', note: 'str', permission: 'str',
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

    # 母子用户APIkey信息查询
    def get_user_apikey_info(self, uid: 'str', access_key: 'str' = None):
        check_should_not_none(uid, 'uid')

        params = {
            "uid": uid,
            "accessKey": access_key
        }
        from huobi.service.subuser.get_user_apikey_info import GetUserApikeyInfoService
        return GetUserApikeyInfoService(params).request(**self.__kwargs)

    # 修改子用户APIkey
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

    # 删除子用户APIkey
    def post_subuser_apikey_deletion(self, sub_uid: 'str', access_key: 'str'):
        check_should_not_none(sub_uid, 'subUid')
        check_should_not_none(access_key, 'accessKey')

        params = {
            "subUid": sub_uid,
            "accessKey": access_key
        }
        from huobi.service.subuser.post_subuser_apikey_deletion import PostSubuserApikeyDeletionService
        return PostSubuserApikeyDeletionService(params).request(**self.__kwargs)

    # 母子用户获取用户UID
    def get_uid(self):
        params = {
        }
        from huobi.service.subuser.get_uid import GetUidService
        return GetUidService(params).request(**self.__kwargs)

    # 设置子用户手续费抵扣模式
    def post_subuser_deduct_mode(self, sub_uids: 'str', deduct_mode: 'str'):
        check_should_not_none(sub_uids, 'subUids')
        check_should_not_none(deduct_mode, 'deductMode')

        params = {
            "subUids": sub_uids,
            "deductMode": deduct_mode
        }
        from huobi.service.subuser.post_subuser_deduct_mode import PostSubuserDeductModeService
        return PostSubuserDeductModeService(params).request(**self.__kwargs)

    # 获取子用户列表
    def get_subuser_user_list(self, from_id: 'int' = None):

        params = {
            "fromId": from_id
        }
        from huobi.service.subuser.get_subuser_user_list import GetSubuserUserListService
        return GetSubuserUserListService(params).request(**self.__kwargs)

    # 获取特定子用户的用户状态
    def get_subuser_user_state(self, sub_uid: 'int'):
        check_should_not_none(sub_uid, 'subUid')
        params = {
            "subUid": sub_uid
        }
        from huobi.service.subuser.get_subuser_user_state import GetSubuserUserStateService
        return GetSubuserUserStateService(params).request(**self.__kwargs)

    # 获取特定子用户的账户列表
    def get_subuser_account_list(self, sub_uid: 'int'):
        check_should_not_none(sub_uid, 'subUid')
        params = {
            "subUid": sub_uid
        }
        from huobi.service.subuser.get_subuser_account_list import GetSubuserAccountListService
        return GetSubuserAccountListService(params).request(**self.__kwargs)

    # 子用户余额（汇总）
    def get_aggregated_subuser_balance(self):
        """
        Get the aggregated balance of all sub-accounts of the current user.

        :return: The balance of all the sub-account aggregated.
        """
        params = {}
        from huobi.service.subuser.get_aggregate_subuser_balance import GetAggregateSubUserBalanceService
        return GetAggregateSubUserBalanceService(params).request(**self.__kwargs)

    # 资产划转（母子用户之间）
    def transfer_between_parent_and_subuser(self, sub_uid: 'int', currency: 'str', amount: 'float',
                                            transfer_type: 'TransferMasterType', client_order_id: 'str'=None):
        """
        Transfer Asset between Parent and Sub Account.

        :param sub_uid: The target sub account uid to transfer to or from. (mandatory)
        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, see {@link TransferMasterType} (mandatory)
        :return: The order id.
        """
        check_currency(currency)
        check_should_not_none(sub_uid, "sub-uid")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "type")

        params = {
            "sub-uid": sub_uid,
            "currency": currency,
            "amount": amount,
            "type": transfer_type,
            "client-order-id": client_order_id
        }
        from huobi.service.subuser.post_subaccount_transfer import PostSubaccountTransferService
        return PostSubaccountTransferService(params).request(**self.__kwargs)

    # 冻结/解冻子用户
    def post_sub_uid_management(self, sub_uid: 'int', action: 'str'):
        """
        use to freeze or unfreeze the sub uid

        :return: user and status.
        """

        check_should_not_none(sub_uid, "subUid")
        check_should_not_none(action, "action")

        params = {
            "subUid": sub_uid,
            "action": action
        }
        from huobi.service.subuser.post_sub_uid_management import PostSubUidManagementService
        return PostSubUidManagementService(params).request(**self.__kwargs)

    # 子用户余额
    def get_account_balance_by_subuid(self, sub_uid):
        """
        Get account balance of a sub-account.

        :param sub_uid: the specified sub account id to get balance for.
        :return: the balance of a sub-account specified by sub-account uid.
        """
        check_should_not_none(sub_uid, "sub-uid")
        params = {
            "sub-uid": sub_uid
        }
        from huobi.service.subuser.get_account_balance_by_subuid import GetAccountBalanceBySubUidService
        return GetAccountBalanceBySubUidService(params).request(**self.__kwargs)

    # 子用户充币地址查询
    def get_sub_user_deposit_address(self, sub_uid: 'int', currency: 'str') -> list:
        """
        Parent get sub user deposit address

        :param sub_uid: Sub user id
        :param currency: Cryptocurrency, like "btc". (mandatory)
        :return:
        """

        check_should_not_none(sub_uid, "subUid")
        check_should_not_none(currency, "currency")
        params = {
            "subUid": sub_uid,
            "currency": currency
        }

        from huobi.service.subuser.get_sub_user_deposit_address import GetSubUserDepositAddressService
        return GetSubUserDepositAddressService(params).request(**self.__kwargs)

    # 子用户充币记录查询
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
        check_should_not_none(sub_uid, "sub_uid")

        params = {
            "subUid": sub_uid,
            "currency": currency,
            "startTime": start_time,
            "endTime": end_time,
            "sort": sort,
            "limit": limit,
            "fromId": from_id
        }

        from huobi.service.subuser.get_sub_user_deposit_history import GetSubUserDepositHistoryService
        return GetSubUserDepositHistoryService(params).request(**self.__kwargs)

    def post_user_initiated_credit(self, transaction_id: 'int', currency: 'str', amount: 'float', account_id: 'int',
                                   user_id: 'int'):
        check_should_not_none(transaction_id, 'transactionId')
        check_should_not_none(currency, 'currency')
        check_should_not_none(amount, 'amount')
        check_should_not_none(account_id, 'accountId')
        check_should_not_none(user_id, 'userId')

        params = {
            "transactionId": transaction_id,
            "currency": currency,
            "amount": amount,
            "accountId": account_id,
            "userId": user_id
        }
        from huobi.service.subuser.post_user_initiated_credit import PostSubuserApikeyGenerationService
        return PostSubuserApikeyGenerationService(params).request(**self.__kwargs)

    # 用户主动授信
    def post_active_credit(self, transaction_id: 'int', currency: 'str', amount: 'float', account_id: 'int', user_id: 'int'):

        check_should_not_none(transaction_id, "transactionId")
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        check_should_not_none(account_id, "accountId")
        check_should_not_none(user_id, "userId")

        params = {
            "transactionId": transaction_id,
            "currency": currency,
            "amount": amount,
            "accountId": account_id,
            "userId": user_id
        }
        from huobi.service.subuser.post_active_credit import PostActiveCreditService
        return PostActiveCreditService(params).request(**self.__kwargs)


