import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection



data ='''
{
	"ch": "market.btcusdt.kline.1min",
	"ts": 1550469651403,
	"tick": {
		"id": 1550469600,
		"open": 3719.880000000000000000,
		"close": 3719.910000000000000000,
		"low": 3719.450000000000000000,
		"high": 3719.990000000000000000,
		"amount": 5.470327974838371482,
		"vol": 20349.203451999999994465900000000000000000,
		"count": 73
	}
}
'''


class TestSubscribeCandlestickEvent(unittest.TestCase):

    def test_request(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_candlestick_event(symbols, CandlestickInterval.MIN1, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("market.btcusdt.kline.1min") != -1)

    def test_request_multi_symbol(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")
        symbols.append("btcht")

        def callback(event):
            pass

        request = impl.subscribe_candlestick_event(symbols, CandlestickInterval.MIN1, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("market.btcusdt.kline.1min") != -1)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("market.btcht.kline.1min") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_candlestick_event(symbols, CandlestickInterval.MIN1, callback)
        candlestick_event = request.json_parser(parse_json_from_string(data))
        self.assertEqual("btcusdt", candlestick_event.symbol)
        self.assertEqual( 1550469651403, candlestick_event.timestamp)
        self.assertEqual(CandlestickInterval.MIN1, candlestick_event.interval)
        self.assertEqual(3719.88, candlestick_event.data.open)
        self.assertEqual(3719.91, candlestick_event.data.close)
        self.assertEqual(3719.45, candlestick_event.data.low)
        self.assertEqual(3719.99, candlestick_event.data.high)
        self.assertEqual(5.470327974838371482, candlestick_event.data.amount)
        self.assertEqual(20349.2034519999999944659, candlestick_event.data.volume)
        self.assertEqual(73, candlestick_event.data.count)






