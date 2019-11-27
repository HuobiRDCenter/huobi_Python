import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
  "op": "notify",
  "topic": "orders.btcusdt",
  "ts": 1522856623232,
  "data": {
    "seq-id": 94984,
    "order-id": 2039498445,
    "symbol": "btcusdt",
    "account-id": 123,
    "order-amount": "5001.000000000000000000",
    "order-price": "1.662100000000000000",
    "created-at": 1522858623622,
    "order-type": "buy-limit",
    "order-source": "api",
    "order-state": "filled",
    "role": "taker|maker",
    "price": "1.662100000000000000",
    "filled-amount": "5000.000000000000000000",
    "unfilled-amount": "2.000000000000000000",
    "filled-cash-amount": "8301.357280000000000000",
    "filled-fees": "8.000000000000000000"
  }
}
'''


class TestSubscribeOrderUpdateEvent(unittest.TestCase):
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
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_order_update(symbols, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("orders.btcusdt") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("12345")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_order_update(symbols, callback)
        event = request.json_parser(parse_json_from_string(data))

        self.assertEqual("btcusdt", event.symbol)
        self.assertEqual(1.6621, event.data.price)
        self.assertEqual(5001, event.data.amount)
        self.assertEqual(5000, event.data.filled_amount)
        self.assertEqual("btcusdt", event.data.symbol)
        self.assertEqual(1522856623232, event.timestamp)
        self.assertEqual(AccountType.SPOT, event.data.account_type)
        self.assertEqual(1522858623622, event.data.created_timestamp)
        self.assertEqual(2039498445, event.data.order_id)
        self.assertEqual(OrderType.BUY_LIMIT, event.data.order_type)
        self.assertEqual(OrderSource.API, event.data.source)
        self.assertEqual(8301.35728, event.data.filled_cash_amount)
        self.assertEqual(8, event.data.filled_fees)


