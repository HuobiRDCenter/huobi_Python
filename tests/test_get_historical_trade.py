import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl


data = '''
{
  "status": "ok",
  "ch": "market.ethusdt.trade.detail",
  "ts": 1550222502992,
  "data": [
    {
      "id": 100416958491,
      "ts": 1550222502562,
      "data": [
        {
          "amount": 0.007100000000000000,
          "ts": 1550222502562,
          "id": 10041695849124569905216,
          "price": 122.180000000000000000,
          "direction": "sell"
        }
      ]
    },
    {
      "id": 100416958394,
      "ts": 1550222501237,
      "data": [
        {
          "amount": 0.489300000000000000,
          "ts": 1550222501237,
          "id": 10041695839424569907865,
          "price": 122.160000000000000000,
          "direction": "sell"
        },
        {
          "amount": 0.735400000000000000,
          "ts": 1551233842487,
          "id": 10041773949425560687111,
          "price": 3804.000000000000000000,
          "direction": "buy"
        }      ]
    }
  ]
}
'''


class TestGetHistoricalTrade(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_historical_trade("btcusdt", "12345", 100)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/market/history/trade") != -1)
        self.assertTrue(request.url.find("symbol=btcusdt") != -1)
        self.assertTrue(request.url.find("size=100") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_historical_trade("btcusdt", "12345", 100)
        trade_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(3, len(trade_list))
        self.assertEqual(122.18, trade_list[0].price)
        self.assertEqual(0.0071, trade_list[0].amount)
        self.assertEqual(1550222502562, trade_list[0].timestamp)
        self.assertEqual(TradeDirection.SELL, trade_list[0].direction)
