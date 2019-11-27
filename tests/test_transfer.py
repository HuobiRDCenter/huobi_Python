import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.exception.huobiapiexception import HuobiApiException

data = '''
{
"status": "ok",
"data": 1000
}
'''


class TestTransfer(unittest.TestCase):
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

    def test_request_in(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.transfer("btcusdt", AccountType.SPOT, AccountType.MARGIN, "btc", 1.1)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("/v1/dw/transfer-in/margin") != -1)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertEqual("btcusdt", request.post_body["symbol"])
        self.assertEqual("btc", request.post_body["currency"])
        self.assertEqual("1.1", request.post_body["amount"])

    def test_request_out(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.transfer("btcusdt", AccountType.MARGIN, AccountType.SPOT, "btc", 2.1)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("/v1/dw/transfer-out/margin") != -1)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertEqual("btcusdt", request.post_body["symbol"])
        self.assertEqual("btc", request.post_body["currency"])
        self.assertEqual("2.1", request.post_body["amount"])

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.transfer("btcusdt", AccountType.MARGIN, AccountType.SPOT, "btc", 2.1)
        self.assertEqual(1000, request.json_parser(parse_json_from_string(data)))

    def test_error_account(self):
        with self.assertRaises(HuobiApiException):
            impl = RestApiRequestImpl("12345", "67890")
            request = impl.transfer("btcusdt", AccountType.OTC, AccountType.SPOT, "btc", 2.1)
