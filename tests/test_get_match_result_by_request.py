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
            "created-at":1550642185237,
            "price":"0.00030503",
            "source":"spot-api",
            "filled-points":"0",
            "filled-fees":"0.00000061006",
            "order-id":24976625673,
            "filled-amount":"1",
            "match-id":100047439757,
            "id":4192759683,
            "type":"sell-market",
            "role":"taker",
            "fee-deduct-currency":""
        },
        {
            "symbol":"htbtc",
            "created-at":1550632074577,
            "price":"0.00030754",
            "source":"spot-api",
            "filled-points":"0.77",
            "filled-fees":"0.00000061508",
            "order-id":24966984923,
            "filled-amount":"1.89",
            "match-id":100047251154,
            "id":4191225853,
            "type":"sell-market",
            "role":"taker",
            "fee-deduct-currency":""
        }
    ]
}


'''


class TestGetMatchResultByRequest(unittest.TestCase):
    def test_request_default_param(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_match_results("btcustd")
        self.assertTrue(request.url.find("/v1/order/matchresults") != -1)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("symbol=btcustd") != -1)
        self.assertTrue(request.url.find("types") == -1)
        self.assertTrue(request.url.find("start-date") == -1)
        self.assertTrue(request.url.find("end-date") == -1)
        self.assertTrue(request.url.find("from") == -1)
        self.assertTrue(request.url.find("size") == -1)

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_match_results("btcustd", OrderType.SELL_LIMIT, "2019-01-03", "2019-02-03", 10, 100)
        self.assertTrue(request.url.find("/v1/order/matchresults") != -1)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("symbol=btcustd") != -1)
        self.assertTrue(request.url.find("types=sell-limit") != -1)
        self.assertTrue(request.url.find("start-date=2019-01-03") != -1)
        self.assertTrue(request.url.find("end-date=2019-02-03") != -1)
        self.assertTrue(request.url.find("from=100") != -1)
        self.assertTrue(request.url.find("size=10") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_match_results("btcustd", OrderType.SELL_LIMIT, "2019-01-03", "2019-02-03", 10, 100)
        match_result_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(match_result_list))
        self.assertEqual(1550632074577, match_result_list[1].created_timestamp)
        self.assertEqual(4191225853, match_result_list[1].id)
        self.assertEqual(100047251154, match_result_list[1].match_id)
        self.assertEqual(24966984923, match_result_list[1].order_id)
        self.assertEqual(1.89, match_result_list[1].filled_amount)
        self.assertEqual(0.00000061508, match_result_list[1].filled_fees)
        self.assertEqual(0.00030754, match_result_list[1].price)
        self.assertEqual("spot-api", match_result_list[1].source)
        self.assertEqual("htbtc", match_result_list[1].symbol)
        self.assertEqual("sell-market", match_result_list[1].order_type)
