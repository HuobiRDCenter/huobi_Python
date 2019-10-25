import unittest
from huobi.connection.impl.restapi_invoker import check_response
from huobi.exception.huobi_api_exception import HuobiApiException

error_date = {
  "ts": "1550209202720",
  "status": "error",
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}

error_date_unexpected = {
  "ts": "1550209202720",
  "status": "abc",
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}


error_data_no_status = {
  "ts": "1550209202720",
  "err-code": "invalid-parameter",
  "err-msg": "invalid symbol"
}


error_etf = {
  "code": "504",
  "data": None,
  "message": "缺少参数:etf_name",
  "success": False
}


class TestErrorResponse(unittest.TestCase):
    def test_error_response(self):
        def test():
            check_response(error_date)

        self.assertRaisesRegex(HuobiApiException, "invalid symbol", test)

    
    def test_error_response_unexpected_response(self):
        def test():
            check_response(error_date_unexpected)
        self.assertRaisesRegex(HuobiApiException, "Response is not expected", test)

    def test_error_response_no_status_response(self):
        def test():
            check_response(error_data_no_status)
        self.assertRaisesRegex(HuobiApiException, "Status cannot be found in response", test)

    def test_error_response_etf(self):
        def test():
            check_response(error_etf)
        self.assertRaisesRegex(HuobiApiException, "etf_name", test)

if __name__ == "__main__":
    unittest.main()