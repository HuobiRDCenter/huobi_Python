import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl



data = '''
{
  "code": 200,
  "data": {
    "etf_name": "hb10",
    "etf_status": 1,
    "purchase_fee_rate": 0.0010,
    "purchase_max_amount": 5000000,
    "purchase_min_amount": 1000,
    "redemption_fee_rate": 0.0020,
    "redemption_max_amount": 5000001,
    "redemption_min_amount": 1001,
    "unit_price": [
      {
        "amount": 0.000126955728465845,
        "currency": "bch"
      },
      {
        "amount": 0.018467942983843364,
        "currency": "eos"
      },
      {
        "amount": 0.425574290019138452,
        "currency": "trx"
      }
    ]
  },
  "message": null,
  "success": true
}
'''


class TestGetEtfSwapConfig(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_etf_swap_config("hb10")
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/etf/swap/config") != -1)
        self.assertTrue(request.url.find("etf_name=hb10") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_etf_swap_config("hb10")
        etf_swap_config = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1000, etf_swap_config.purchase_min_amount)
        self.assertEqual(5000000, etf_swap_config.purchase_max_amount)
        self.assertEqual(1001, etf_swap_config.redemption_min_amount)
        self.assertEqual(5000001, etf_swap_config.redemption_max_amount)
        self.assertEqual(0.001, etf_swap_config.purchase_fee_rate)
        self.assertEqual(0.002, etf_swap_config.redemption_fee_rate)
        self.assertEqual(EtfStatus.NORMAL, etf_swap_config.status)
        self.assertEqual(3, len(etf_swap_config.unit_price_list))
        self.assertEqual(0.018467942983843364, etf_swap_config.unit_price_list[1].amount)
        self.assertEqual("eos", etf_swap_config.unit_price_list[1].currency)
