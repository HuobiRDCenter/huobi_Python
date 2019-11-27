import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl



data = '''
{
  "status": "ok",
  "ch": "market.ethusdt.detail.merged",
  "ts": 1550223581490,
  "tick": {
    "amount": 222930.8868295491,
    "open": 122.4,
    "close": 122.24,
    "high": 123.42,
    "id": 100417063447,
    "count": 68987,
    "low": 120.25,
    "version": 100417063447,
    "ask": [
      122.26,
      0.8271
    ],
    "vol": 27123490.874530632,
    "bid": [
      122.24,
      2.6672
    ]
  }
}
'''


class TestGetBestQuote(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_best_quote("btcusdt")
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/market/detail/merged") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_best_quote("btcusdt")
        best_quote = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1550223581490, best_quote.timestamp)
        self.assertEqual(122.26, best_quote.ask_price)
        self.assertEqual(0.8271, best_quote.ask_amount)
        self.assertEqual(122.24, best_quote.bid_price)
        self.assertEqual(2.6672, best_quote.bid_amount)

