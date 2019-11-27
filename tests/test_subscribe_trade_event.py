import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection

from huobi.impl.restapirequestimpl import account_info_map


data ='''
{
	"ch": "market.btcusdt.trade.detail",
	"ts": 1550558574702,
	"tick": {
		"id": 100335442624,
		"ts": 1550558574684,
		"data": [{
			"amount": 0.001000000000000000,
			"ts": 1550558574684,
			"id": 10033544262424890651900,
			"price": 3892.360000000000000000,
			"direction": "sell"
		}, {
			"amount": 0.051200000000000000,
			"ts": 1550558574684,
			"id": 10033544262424890651183,
			"price": 3892.350000000000000000,
			"direction": "buy"
		}]
	}
}
'''


class TestSubscribeTradeEvent(unittest.TestCase):

    def test_request(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_trade_event(symbols, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("market.btcusdt.trade.detail") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_trade_event(symbols, callback)
        event = request.json_parser(parse_json_from_string(data))
        self.assertEqual("btcusdt", event.symbol)
        self.assertEqual(2, len(event.trade_list))
        self.assertEqual(1550558574702, event.timestamp)
        self.assertEqual(0.001, event.trade_list[0].amount)
        self.assertEqual(1550558574684, event.trade_list[0].timestamp)
        self.assertEqual("10033544262424890651900", event.trade_list[0].trade_id)
        self.assertEqual(3892.36, event.trade_list[0].price)
        self.assertEqual(TradeDirection.SELL, event.trade_list[0].direction)
        self.assertEqual(0.0512, event.trade_list[1].amount)
        self.assertEqual(1550558574684, event.trade_list[1].timestamp)
        self.assertEqual("10033544262424890651183", event.trade_list[1].trade_id)
        self.assertEqual(3892.35, event.trade_list[1].price)
        self.assertEqual(TradeDirection.BUY, event.trade_list[1].direction)
