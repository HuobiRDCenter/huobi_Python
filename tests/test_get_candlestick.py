import unittest
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.model.constant import *

data = '''{
  "status": "ok",
  "ch": "market.btcusdt.kline.1day",
  "ts": 1550197964381,
  "data": [
    {
      "id": 1550160000,
      "open": 3600.770000000000000000,
      "close": 3602.380000000000000000,
      "low": 3575.000000000000000000,
      "high": 3612.190000000000000000,
      "amount": 4562.766744240224615720,
      "vol": 16424799.084153959200406053550000000000000000,
      "count": 28891
    },
    {
      "id": 1550073600,
      "open": 3594.850000000000000000,
      "close": 3600.790000000000000000,
      "low": 3570.000000000000000000,
      "high": 3624.300000000000000000,
      "amount": 14514.049885396099061006,
      "vol": 52311364.004324447892964650980000000000000000,
      "count": 99003
    }
  ]
}
'''


class TestGetCandlestick(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_candlestick("btcusdt", CandlestickInterval.YEAR1, 100)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/market/history/kline") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)
        self.assertTrue(request.url.find("period=1year") != -1)
        self.assertTrue(request.url.find("size=100"))

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_candlestick("btcusdt", CandlestickInterval.YEAR1, 100)
        candlestick_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(candlestick_list))
        self.assertEqual(1550160000, candlestick_list[0].id)
        self.assertEqual(3612.19, candlestick_list[0].high)
        self.assertEqual(3575, candlestick_list[0].low)
        self.assertEqual(3600.77, candlestick_list[0].open)
        self.assertEqual(3602.38, candlestick_list[0].close)
        self.assertEqual(4562.76674424022461572, candlestick_list[0].amount)
        self.assertEqual(16424799.08415395920040605355, candlestick_list[0].volume)
        self.assertEqual(28891, candlestick_list[0].count)
        self.assertEqual(1550073600, candlestick_list[1].id)
        self.assertEqual(3624.3, candlestick_list[1].high)
        self.assertEqual(3570, candlestick_list[1].low)
        self.assertEqual(3594.85, candlestick_list[1].open)
        self.assertEqual(3600.79, candlestick_list[1].close)
        self.assertEqual(14514.049885396099061006, candlestick_list[1].amount)
        self.assertEqual(52311364.00432444789296465098, candlestick_list[1].volume)
        self.assertEqual(99003, candlestick_list[1].count)
