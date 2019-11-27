import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl


data = '''
{
  "status": "ok",
  "ch": "market.ethusdt.detail",
  "ts": 1550224944129,
  "tick": {
    "amount": 224419.35108158883,
    "open": 121.84,
    "close": 121.97,
    "high": 123.42,
    "id": 100417200521,
    "count": 69299,
    "low": 120.25,
    "version": 100417200521,
    "vol": 27305221.739623416
  }
}
'''

class TestGet24HTradeStatistics(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_24h_trade_statistics("btcusdt")
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/market/detail") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_24h_trade_statistics("btcusdt")
        trade_statistics = request.json_parser(parse_json_from_string(data))
        self.assertEqual(224419.35108158883, trade_statistics.amount)
        self.assertEqual(121.97, trade_statistics.close)
        self.assertEqual(123.42, trade_statistics.high)
        self.assertEqual(120.25, trade_statistics.low)
        self.assertEqual(121.84, trade_statistics.open)
        self.assertEqual(27305221.739623416, trade_statistics.volume)
        self.assertEqual(69299, trade_statistics.count)
