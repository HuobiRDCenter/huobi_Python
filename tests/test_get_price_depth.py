import unittest
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl


data = '''
    {
  "status": "ok",
  "ch": "market.ethusdt.depth.step0",
  "ts": 1550218546616,
  "tick": {
    "bids": [
      [
        122.920000000000000000,
        2.746800000000000000
      ],
	  [
        120.300000000000000000,
        494.745900000000000000
      ]
    ],
    "asks": [
      [
        122.940000000000000000,
        67.554900000000000000
      ],
	  [
        124.620000000000000000,
        50.000000000000000000
      ]
    ],
    "ts": 1550218546020,
    "version": 100416549839
  }
}
'''


class TestGetPriceDepth(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_price_depth("btcustd", 10)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/market/depth") != -1)
        self.assertTrue(request.url.find("symbol=btcustd") != -1)
        self.assertTrue(request.url.find("type=step0") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_price_depth("btcustd", 1)
        price_depth = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1, len(price_depth.bids))
        self.assertEqual(1550218546020, price_depth.timestamp)
        self.assertEqual(122.92, price_depth.bids[0].price)
        self.assertEqual(2.7468, price_depth.bids[0].amount)
        self.assertEqual(122.94, price_depth.asks[0].price)
        self.assertEqual(67.5549, price_depth.asks[0].amount)


if __name__ == '__main__':
    unittest.main()
