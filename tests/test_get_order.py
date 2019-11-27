import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
    "status":"ok",
    "data":{
        "id":24962048654,
        "symbol":"htbtc",
        "account-id":123,
        "amount":"1.000000000000000000",
        "price":"1.00000123000000000000",
        "created-at":1550626936504,
        "type":"sell-limit",
        "field-amount":"0.08888",
        "field-cash-amount":"0.204",
        "field-fees":"0.0345",
        "finished-at":1550626936798,
        "source":"api",
        "state":"canceled",
        "canceled-at":1550626936722
    }
}'''


class TestGetOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        user = User()
        account = Account()
        account.account_type = AccountType.SPOT
        account.id = 123
        account1 = Account()
        account1.account_type = AccountType.SPOT
        account1.id = 456
        accounts = list()
        accounts.append(account)
        accounts.append(account1)
        user.accounts = accounts
        account_info_map.user_map["12345"] = user

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_order("htbtc", 24962048654)
        url = "/v1/order/orders/24962048654"
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find(url) != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_order("htbtc", 24962048654)
        order = request.json_parser(parse_json_from_string(data))

        self.assertEqual(1550626936504, order.created_timestamp)
        self.assertEqual(AccountType.SPOT, order.account_type)
        self.assertEqual(1550626936722, order.canceled_timestamp)
        self.assertEqual(1550626936798, order.finished_timestamp)
        self.assertEqual(24962048654, order.order_id)
        self.assertEqual(0.08888, order.filled_amount)
        self.assertEqual(0.204, order.filled_cash_amount)
        self.assertEqual(0.0345, order.filled_fees)
        self.assertEqual(1.00000123, order.price)
        self.assertEqual("htbtc", order.symbol)
        self.assertEqual(1, order.amount)
        self.assertEqual(OrderSource.API, order.source)
        self.assertEqual(OrderState.CANCELED, order.state)
        self.assertEqual(OrderType.SELL_LIMIT, order.order_type)
