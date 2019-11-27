import unittest
import json
from huobi.model import *
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.impl.restapiinvoker import check_response
from huobi.exception.huobiapiexception import HuobiApiException

error_date = '''
{
  "ts": 1550209202720,
  "status": "error",
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}'''

error_date_unexpected = '''
{
  "ts": 1550209202720,
  "status": "abc",
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}
'''

error_data_no_status = '''
{
  "ts": 1550209202720,
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}
'''

error_etf = '''
{
  "code": 504,
  "data": null,
  "message": "缺少参数:etf_name",
  "success": false
}
'''


class TestErrorResponse(unittest.TestCase):

    def test_error_response(self):
        def test():
            json_wrapper = parse_json_from_string(error_date)
            check_response(json_wrapper)
        self.assertRaisesRegex(HuobiApiException, "invalid symbol", test)

    def test_error_response_unexpected_response(self):
        def test():
            json_wrapper = parse_json_from_string(error_date_unexpected)
            check_response(json_wrapper)
        self.assertRaisesRegex(HuobiApiException, "Response is not expected", test)

    def test_error_response_no_status_response(self):
        def test():
            json_wrapper = parse_json_from_string(error_data_no_status)
            check_response(json_wrapper)
        self.assertRaisesRegex(HuobiApiException, "Status cannot be found in response", test)

    def test_error_response_etf(self):
        def test():
            json_wrapper = parse_json_from_string(error_etf)
            check_response(json_wrapper)
        self.assertRaisesRegex(HuobiApiException, "etf_name", test)
