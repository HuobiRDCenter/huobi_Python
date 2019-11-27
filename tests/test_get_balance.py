import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
	"status": "ok",
	"data": {
		"id": 5628009,
		"type": "spot",
		"state": "working",
		"list": [{
			"currency": "lun",
			"type": "trade",
			"balance": "0"
		}, {
			"currency": "phx",
			"type": "frozen",
			"balance": "0"
		}]
	}
}
'''


class TestGetBalance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User()
        account = Account()
        account.account_type = AccountType.SPOT
        account.id = 12345
        accounts = list()
        accounts.append(account)
        user.accounts = accounts
        account_info_map.user_map["12345"] = user

    def test_request(self):
        account = Account()
        account.id = 5628009
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_balance(account)
        self.assertTrue(request.url.find("/v1/account/accounts/5628009/balance") != -1)
        self.assertTrue(request.url.find("Signature") != -1)

    def test_result(self):
        account = Account()
        account.id = 5628009
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_balance(account)
        balances = request.json_parser(parse_json_from_string(data))
        self.assertEqual("lun", balances[0].currency)
        self.assertEqual(0, balances[0].balance)
        self.assertEqual(BalanceType.TRADE, balances[0].balance_type)



