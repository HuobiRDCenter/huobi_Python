from huobi.client.subuser import SubuserClient
from huobi.constant import *
from huobi.utils import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)

subUids = '159284259'
accountType = SubuserTradePrivilegeType.MARGIN
activation = SubUserTradeStatus.DEACTIVATED

subUserList = subuser_client.post_set_tradable_market(subUids, accountType, activation)
LogInfo.output_list(subUserList)
