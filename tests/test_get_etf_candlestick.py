import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl



data = '''
{
  "code": 200,
  "success": "True",
  "data": [
{
    "id": 1499184000,
    "amount": 123.123,
    "open": 0.7794,
    "close": 0.779,
    "low": 0.769,
    "high": 0.7694,
    "vol": 456.456
  }
]
}
'''


class TestGetETFCandlestick(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_etf_candlestick("hb10", CandlestickInterval.YEAR1, 100)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/quotation/market/history/kline") != -1)
        self.assertTrue(request.url.find("symbol=hb10"))
        self.assertTrue(request.url.find("period=1year"))
        self.assertTrue(request.url.find("limit=100"))

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_etf_candlestick("hb10", CandlestickInterval.YEAR1, 100)
        candlestick_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1, len(candlestick_list))
        self.assertEqual(0, candlestick_list[0].id)
        self.assertEqual(0.7694, candlestick_list[0].high)
        self.assertEqual(0.769, candlestick_list[0].low)
        self.assertEqual(0.7794, candlestick_list[0].open)
        self.assertEqual(0.779, candlestick_list[0].close)
        self.assertEqual(123.123, candlestick_list[0].amount)
        self.assertEqual(456.456, candlestick_list[0].volume)
