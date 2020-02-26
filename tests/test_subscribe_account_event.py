import unittest
import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection

from huobi.impl.restapirequestimpl import account_info_map


data ='''
{
	"op": "notify",
	"ts": 1550556381242,
	"topic": "accounts",
	"data": {
		"event": "order-place",
		"list": [{
			"account-id": 123,
			"currency": "ht",
			"type": "trade",
			"balance": "10.8208984536412"
		}]
	}
}
'''


class TestSubscribeAccountEvent(unittest.TestCase):
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
        impl = WebsocketRequestImpl("12345")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_account_event(BalanceMode.AVAILABLE, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("accounts") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("12345")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_account_event(BalanceMode.AVAILABLE, callback)
        event = request.json_parser(parse_json_from_string(data))

        self.assertEqual(1550556381242, event.timestamp)
        self.assertEqual(1, len(event.account_change_list))
        print(event)
        print(event.change_type)
        self.assertEqual(AccountChangeType.ORDER_PLACE, event.change_type)
        self.assertEqual(AccountType.SPOT, event.account_change_list[0].account_type)
        self.assertEqual("ht", event.account_change_list[0].currency)
        self.assertEqual(10.8208984536412, event.account_change_list[0].balance)
        self.assertEqual(BalanceType.TRADE, event.account_change_list[0].balance_type)
