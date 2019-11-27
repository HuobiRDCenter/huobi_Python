import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl



data = '''
{
  "code": 200,
  "data": [
    {
      "id": 112222,
      "gmt_created": 1528855872323,
      "currency": "hb10",
      "amount": 11.5,
      "type": 1,
      "status": 2,
      "detail": {
        "used_currency_list": [
          {
            "currency": "btc",
            "amount": 0.666
          },
          {
            "currency": "eth",
            "amount": 0.666
          }
        ],
        "rate": 0.002,
        "fee": 100.11,
        "point_card_amount":1.0,
        "obtain_currency_list": [
          {
            "currency": "hb10",
            "amount": 1000
          }
        ]
      }
    },
    {
      "id": 112223,
      "gmt_created": 1528855872323,
      "currency": "hb10",
      "amount": 11.5,
      "type": 2,
      "status": 1,
      "detail": {
        "used_currency_list": [
          {
            "currency": "btc",
            "amount": 0.666
          },
          {
            "currency": "eth",
            "amount": 0.666
          }
        ],
        "rate": 0.002,
        "fee": 100.11,
        "point_card_amount":1.0,
        "obtain_currency_list": [
          {
            "currency": "hb10",
            "amount": 1000
          }
        ]
      }
    }
  ],
  "message": null,
  "success": true
}
'''


class TestGetEtfSwapHistory(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_etf_swap_history("hb10", 0, 10)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/etf/swap/list") != -1)
        self.assertTrue(request.url.find("etf_name=hb10") != -1)
        self.assertTrue(request.url.find("offset=0") != -1)
        self.assertTrue(request.url.find("limit=10") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_etf_swap_history("hb10", 0, 10)
        etf_swap_history_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(etf_swap_history_list))
        self.assertEqual(1528855872323, etf_swap_history_list[0].created_timestamp)
        self.assertEqual("hb10", etf_swap_history_list[0].currency)
        self.assertEqual(11.5, etf_swap_history_list[0].amount)
        self.assertEqual(EtfSwapType.IN, etf_swap_history_list[0].type)
        self.assertEqual(2, len(etf_swap_history_list[0].used_currency_list))
        self.assertEqual("btc", etf_swap_history_list[0].used_currency_list[0].currency)
        self.assertEqual(0.666, etf_swap_history_list[0].used_currency_list[0].amount)
        self.assertEqual(0.002, etf_swap_history_list[0].rate)
        self.assertEqual(100.11, etf_swap_history_list[0].fee)
        self.assertEqual(2, etf_swap_history_list[0].status)
        self.assertEqual(1, etf_swap_history_list[0].point_card_amount)
        self.assertEqual(1, len(etf_swap_history_list[0].obtain_currency_list))
        self.assertEqual("hb10", etf_swap_history_list[0].obtain_currency_list[0].currency)
        self.assertEqual(1000, etf_swap_history_list[0].obtain_currency_list[0].amount)
