import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.impl.restapirequestimpl import account_info_map


class TestCancelOrder(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.cancel_order("btcusdt", 12345)
        path = "/v1/order/orders/{}/submitcancel"
        path = path.format(12345)
        self.assertTrue(request.url.find(path) != -1)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("Signature") != -1)

    def test_request_cancel_orders(self):
        order_id_list = list()
        order_id_list.append(12443)
        order_id_list.append(2344)
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.cancel_orders("htbtc", order_id_list)
        self.assertTrue(request.url.find("/v1/order/orders/batchcancel") != -1)
        self.assertEqual("POST", request.method)
        self.assertEqual("12443", request.post_body["order-ids"][0])
        self.assertEqual("2344", request.post_body["order-ids"][1])


