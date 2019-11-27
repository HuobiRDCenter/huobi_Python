import unittest
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.model import *
from huobi.impl.utils import *
from huobi.model import *
from tests.mock_websocket_connection import MockWebsocketConnection

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
    "ch":"market.btcusdt.detail",
    "ts":1550740513421,
    "tick":{
        "amount":29147.328607142535,
        "open":3.0342E-4,
        "close":3947.03,
        "high":4015,
        "id":100359274519,
        "count":204966,
        "low":3903.5,
        "version":100359274519,
        "vol":115320213.26007387
    }
}
'''


class TestSubscribeTradeStatistics(unittest.TestCase):
    def test_request(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_24h_trade_statistics_event(symbols, callback)
        mock_connection = MockWebsocketConnection(request)
        request.subscription_handler(mock_connection)
        subscription = mock_connection.pop_output_message()
        self.assertTrue(subscription.find("btcusdt.detail") != -1)

    def test_result(self):
        impl = WebsocketRequestImpl("")
        symbols = list()
        symbols.append("btcusdt")

        def callback(event):
            pass

        request = impl.subscribe_24h_trade_statistics_event(symbols, callback)
        event = request.json_parser(parse_json_from_string(data))
        self.assertEqual("btcusdt", event.symbol);
        self.assertEqual(1550740513421, event.timestamp);
        self.assertEqual(204966, event.trade_statistics.count)
        self.assertEqual(115320213.26007387, event.trade_statistics.volume)
        self.assertEqual(0.00030342, event.trade_statistics.open)
        self.assertEqual(3903.5, event.trade_statistics.low)
        self.assertEqual(4015, event.trade_statistics.high)
        self.assertEqual(3947.03, event.trade_statistics.close)
        self.assertEqual(29147.328607142535, event.trade_statistics.amount)
