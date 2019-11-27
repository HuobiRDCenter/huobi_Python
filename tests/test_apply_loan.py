import unittest
from huobi.model import *
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
"status": "ok",
"data": 1000
}
'''


class TestApplyLoan(unittest.TestCase):

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
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.apply_loan("btcusdt", "btc", 1.1)
        self.assertEqual("POST", request.method)
        self.assertEqual("btcusdt", request.post_body["symbol"])
        self.assertEqual("btc", request.post_body["currency"])
        self.assertEqual("1.1", request.post_body["amount"])

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.apply_loan("btcusdt", "btc", 2.1)
        self.assertEqual(1000, request.json_parser(parse_json_from_string(data)))
