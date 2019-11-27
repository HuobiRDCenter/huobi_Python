import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''

{
    "status":"ok",
    "data":[
        {
            "symbol":"htbtc",
            "created-at":1550632074577,
            "filled-points":"0",
            "source":"spot-api",
            "price":"0.00030754",
            "filled-amount":"1",
            "filled-fees":"0.00000061508",
            "match-id":100047251154,
            "order-id":24966984923,
            "id":4191225853,
            "type":"sell-market",
            "fee-deduct-currency":"",
            "role":"taker"
        },
        {
            "symbol":"htbtc",
            "created-at":1550632074577,
            "filled-points":"0",
            "source":"spot-api",
            "price":"0.00030754",
            "filled-amount":"1",
            "filled-fees":"0.00000061508",
            "match-id":100047251154,
            "order-id":24966984923,
            "id":4191225853,
            "type":"sell-market",
            "fee-deduct-currency":"",
            "role":"taker"
        }
    ]
}
'''


class TestGetMatchResultByOrderId(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_match_results_by_order_id("htbtc", 24966984923)
        path = "/v1/order/orders/{}/matchresults"
        path = path.format(24966984923)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find(path) != -1)
        self.assertTrue(request.url.find("Signature") != -1)

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_match_results("htbtc", 24966984923)
        match_result_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(match_result_list))
        self.assertEqual(1550632074577, match_result_list[0].created_timestamp)
        self.assertEqual(4191225853, match_result_list[0].id)
        self.assertEqual(100047251154, match_result_list[0].match_id)
        self.assertEqual(24966984923, match_result_list[0].order_id)
        self.assertEqual(1, match_result_list[0].filled_amount)
        self.assertEqual(0.00000061508, match_result_list[0].filled_fees)
        self.assertEqual(0.00030754, match_result_list[0].price)
        self.assertEqual("spot-api", match_result_list[0].source)
        self.assertEqual("sell-market", match_result_list[0].order_type)
