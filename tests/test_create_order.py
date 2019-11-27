import unittest
from huobi.model import *
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map

data = '''{"status":"ok","data":"24876987459"}
'''


class TestCreateOrder(unittest.TestCase):

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
        request = impl.create_order("btcusdt", AccountType.SPOT, OrderType.SELL_LIMIT, 1.0, 1.0)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("Signature") != 1)
        self.assertEqual("btcusdt", request.post_body["symbol"])
        self.assertEqual("12345", request.post_body["account-id"])
        self.assertEqual("1.0", request.post_body["amount"])
        self.assertEqual("1.0", request.post_body["price"])
        self.assertEqual(OrderType.SELL_LIMIT, request.post_body["type"])
        self.assertEqual("api", request.post_body["source"])

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.create_order("btcusdt", AccountType.SPOT, OrderType.SELL_LIMIT, 1.0, 1.0)
        order_id = request.json_parser(parse_json_from_string(data))
        self.assertEqual(24876987459, order_id)
