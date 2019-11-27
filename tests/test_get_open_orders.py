import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map

data = '''
{
	"status": "ok",
	"data": [{
			"created-at": 1550628731111,
			"symbol": "htbtc",
			"source": "api",
			"amount": "1.000000000000000000",
			"account-id": 123,
			"filled-amount": "0.1",
			"filled-cash-amount": "0.2",
			"filled-fees": "0.3",
			"price": "1.100000000000000000",
			"id": 24963751000,
			"state": "submitted",
			"type": "sell-limit"
		},
		{
			"created-at": 1550628730000,
			"symbol": "htbtc",
			"source": "api",
			"amount": "2.000000000000000000",
			"account-id": 456,
			"filled-amount": "2.0",
			"filled-cash-amount": "2.1",
			"filled-fees": "2.2",
			"price": "2.100000000000000000",
			"id": 24963751111,
			"state": "submitted",
			"type": "buy-limit"
		}
	]
}
'''

class TestGetOpenOrders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User()
        account = Account()
        account.account_type = AccountType.SPOT
        account.id = 123
        accounts = list()
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
        request = impl.get_open_orders("btcusdt", AccountType.SPOT, 10, OrderSide.BUY)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/order/openOrders") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)
        self.assertTrue(request.url.find("size=10") != -1)
        self.assertTrue(request.url.find("side=buy") != -1)
        self.assertTrue(request.url.find("account-id=123") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_open_orders("btcusdt", AccountType.SPOT, 10, OrderSide.BUY)
        order_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(order_list))
        self.assertEqual("htbtc", order_list[0].symbol)
        self.assertEqual(1, order_list[0].amount)
        self.assertEqual(1.1, order_list[0].price)
        self.assertEqual(0.1, order_list[0].filled_amount)
        self.assertEqual(0.2, order_list[0].filled_cash_amount)
        self.assertEqual(0.3, order_list[0].filled_fees)
        self.assertEqual(24963751000, order_list[0].order_id)
        self.assertEqual(AccountType.SPOT, order_list[0].account_type)
        self.assertEqual(OrderState.SUBMITTED, order_list[0].state)
        self.assertEqual(OrderType.SELL_LIMIT, order_list[0].order_type)
        self.assertEqual(1550628731111, order_list[0].created_timestamp)
