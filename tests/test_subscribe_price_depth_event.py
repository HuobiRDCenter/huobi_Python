import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection

from huobi.impl.restapirequestimpl import account_info_map

data = '''
{
	"ch": "market.btcusdt.depth.step0",
	"ts": 1550558788054,
	"tick": {
		"bids": [
			[3891.940000000000000000, 0.025700000000000000],
			[3891.610000000000000000, 0.710000000000000000],
			[3891.500000000000000000, 0.001000000000000000]
		],
		"asks": [
			[3891.950000000000000000, 0.028300000000000000],
			[3891.990000000000000000, 1.103500000000000000]
		],
		"ts": 1550558788026,
		"version": 100335470482
	}
}
'''

class TestSubscribePriceDepthEvent(unittest.TestCase):
    def test_request(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_price_depth_event(symbols, "step0", callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("market.btcusdt.depth.step0") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_price_depth_event(symbols, "step0",callback)
        event = request.json_parser(parse_json_from_string(data))
        self.assertEqual("btcusdt", event.symbol)
        self.assertEqual(1550558788054, event.timestamp)
        self.assertEqual(3, len(event.data.bids))
        self.assertEqual(2, len(event.data.asks))
        self.assertEqual(3891.94, event.data.bids[0].price)
        self.assertEqual(0.0257, event.data.bids[0].amount)
        self.assertEqual(3891.95, event.data.asks[0].price)
        self.assertEqual(0.0283, event.data.asks[0].amount)
