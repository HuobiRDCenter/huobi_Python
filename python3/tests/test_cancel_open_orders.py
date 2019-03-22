import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.impl.restapirequestimpl import account_info_map


data = '''
{"status":"ok","data":{"success-count":5,"failed-count":0,"next-id":-1}}
'''


class TestCancelOpenOrders(unittest.TestCase):

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
        request = impl.cancel_open_orders("htbtc", AccountType.SPOT, OrderSide.BUY, 30)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("symbol=htbtc") != -1)
        self.assertTrue(request.url.find("account-id=12345") != -1)
        self.assertTrue(request.url.find("side=buy") != -1)
        self.assertTrue(request.url.find("size=30") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.cancel_open_orders("htbtc", AccountType.SPOT, OrderSide.BUY, 30)
        result = request.json_parser(parse_json_from_string(data))
        self.assertEqual(0, result.failed_count)
        self.assertEqual(5, result.success_count)
