import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{"status": "ok", "data": 1000}
'''


class TestTransferMaster(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.transfer_between_parent_and_sub(123, "btc", 1.2, TransferMasterType.IN)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("/v1/subuser/transfer") != -1)
        self.assertTrue(123, request.post_body["sub-uid"])
        self.assertTrue("btc", request.post_body["currency"])
        self.assertTrue("master-transfer-in", request.post_body["type"])
        self.assertTrue("1.2", request.post_body["type"])

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.transfer_between_parent_and_sub(123, "btc", 1.2, TransferMasterType.IN)
        value = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1000, value)


