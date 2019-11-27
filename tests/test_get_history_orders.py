import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map

data = '''
{
    "status":"ok",
    "data":[
        {
            "id":24965104183,
            "symbol":"htbtc",
            "account-id":12345,
            "amount":"1.000000000000000000",
            "price":"1.000000000000000001",
            "created-at":1550630155350,
            "type":"sell-limit",
            "field-amount":"0.0888",
            "field-cash-amount":"0.011",
            "field-fees":"0.03445",
            "finished-at":1550630155647,
            "source":"api",
            "state":"canceled",
            "canceled-at":1550630155568
        },
        {
            "id":24965089728,
            "symbol":"htbtc",
            "account-id":12345,
            "amount":"1.000000000000000000",
            "price":"1.000000000000000000",
            "created-at":1550630140288,
            "type":"sell-limit",
            "field-amount":"0.0",
            "field-cash-amount":"0.0",
            "field-fees":"0.0",
            "source":"api",
            "state":"canceled"
                }
    ]
}
'''


class TestGetHistoryOrders(unittest.TestCase):
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
        request = impl.get_historical_orders("btcusdt", OrderState.CANCELED, OrderType.SELL_LIMIT, "2019-01-03", "2019-02-03", 123, 456)

        self.assertTrue(request.url.find("/v1/order/orders") != -1)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("Signature") != -1)

        self.assertTrue(request.url.find("symbol=btcusdt") != -1)
        self.assertTrue(request.url.find("states=canceled") != -1)
        self.assertTrue(request.url.find("start-date=2019-01-03") != -1)
        self.assertTrue(request.url.find("end-date=2019-02-03") != -1)
        self.assertTrue(request.url.find("types=sell-limit") != -1)
        self.assertTrue(request.url.find("from=123") != -1)
        self.assertTrue(request.url.find("size=456") != -1)

    def test_request_dep_param(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_historical_orders("btcusdt", OrderState.CANCELED)
        self.assertTrue(request.url.find("/v1/order/orders") != -1)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)
        self.assertTrue(request.url.find("states=canceled") != -1)
        self.assertTrue(request.url.find("start-date") == -1)
        self.assertTrue(request.url.find("end-date") == -1)
        self.assertTrue(request.url.find("types") == -1)
        self.assertTrue(request.url.find("from") == -1)
        self.assertTrue(request.url.find("size") == -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_historical_orders("btcusdt", OrderState.CANCELED, OrderType.SELL_LIMIT, "2019-01-03", "2019-02-03", 123, 456)
        order_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(order_list))
        self.assertEqual(24965104183, order_list[0].order_id)
        self.assertEqual(AccountType.SPOT, order_list[0].account_type)
        self.assertEqual(1550630155568, order_list[0].canceled_timestamp)
        self.assertEqual(1550630155647, order_list[0].finished_timestamp)
        self.assertEqual(1550630155350, order_list[0].created_timestamp)
        self.assertEqual(0.0888, order_list[0].filled_amount)
        self.assertEqual(0.011, order_list[0].filled_cash_amount)
        self.assertEqual(0.03445, order_list[0].filled_fees)
        self.assertEqual(1.000000000000000001, order_list[0].price)
        self.assertEqual("htbtc", order_list[0].symbol)
        self.assertEqual(1, order_list[0].amount)
        self.assertEqual(OrderSource.API, order_list[0].source)
        self.assertEqual(OrderState.CANCELED, order_list[0].state)
        self.assertEqual(OrderType.SELL_LIMIT, order_list[0].order_type)
        self.assertEqual(0, order_list[1].finished_timestamp)
        self.assertEqual(0, order_list[1].canceled_timestamp)
