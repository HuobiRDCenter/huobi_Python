import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.exception.huobiapiexception import HuobiApiException

data = '''
{
	"status": "ok",
	"data": [{
			"loan-balance": "0.100000000000000000",
			"interest-balance": "0.000200000000000000",
			"interest-rate": "0.002000000000000000",
			"loan-amount": "0.110000000000000000",
			"accrued-at": 1511169724000,
			"interest-amount": "0.001200000000000000",
			"symbol": "ethbtc",
			"currency": "btc",
			"id": 390,
			"deduct-rate":1.201,
			"paid-point":10.87,
			"state": "accrual",
			"account-id": 123,
			"user-id": 119910,
			"created-at": 1511169724530,
			"deduct-currency":"",
			"paid-coin":0,
			"deduct-amount":0.1,
			"updated-at":1511169724531
		},
		{
			"loan-balance": "1.100000000000000000",
			"interest-balance": "1.000200000000000000",
			"interest-rate": "1.002000000000000000",
			"loan-amount": "1.110000000000000000",
			"accrued-at": 1511169724531,
			"interest-amount": "1.001200000000000000",
			"symbol": "ethbtc",
			"currency": "btc",
			"id": 391,
			"paid-point":10.87,
			"deduct-rate":1.201,
			"state": "accrual",
			"account-id": 456,
			"user-id": 119911,
			"created-at": 1511169724531,
			"deduct-currency":"",
			"paid-coin":0,
			"deduct-amount":0.1,
			"updated-at":1511169724531
		}
	]
}
'''


class TestGetLoanHistory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        user = User()
        account = Account()
        account.account_type = AccountType.SPOT
        account.id = 123
        accounts = list()
        account1 = Account()
        account1.account_type = AccountType.SPOT
        account1.id = 456
        accounts = list()
        accounts.append(account)
        accounts.append(account1)
        user.accounts = accounts
        account_info_map.user_map["12345"] = user

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_loan("btcusdt", "2019-01-02", "2019-02-03", LoanOrderState.CREATED, 23456, 123)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/margin/loan-orders") != -1)
        self.assertTrue(request.url.find("start-date=2019-01-02") != -1)
        self.assertTrue(request.url.find("end-date=2019-02-03") != -1)
        self.assertTrue(request.url.find("states=created") != -1)
        self.assertTrue(request.url.find("from=23456") != -1)
        self.assertTrue(request.url.find("size=123") != -1)
        self.assertTrue(request.url.find("driect") == -1)

    def test_def_param(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_loan("btcusdt", None, None, None, None)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/margin/loan-orders") != -1)
        self.assertTrue(request.url.find("start-date") == -1)
        self.assertTrue(request.url.find("end-date") == -1)
        self.assertTrue(request.url.find("states") == -1)
        self.assertTrue(request.url.find("from") == -1)
        self.assertTrue(request.url.find("size") == -1)
        self.assertTrue(request.url.find("driect") == -1)

    def test_error(self):
        def test():
            impl = RestApiRequestImpl("12345", "67890")
            request = impl.get_loan("btcusdt", "2019-01-2t", "2019-02-03", LoanOrderState.CREATED, 23456, 123)
        self.assertRaisesRegex(HuobiApiException, "is not invalid date format", test)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_loan("btcusdt", "2019-01-02", "2019-02-03", LoanOrderState.CREATED, 23456, 123)
        loan_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(loan_list))
        self.assertEqual(390, loan_list[0].id)
        self.assertEqual(0.1, loan_list[0].loan_balance)
        self.assertEqual(0.0002, loan_list[0].interest_balance)
        self.assertEqual(0.002, loan_list[0].interest_rate)
        self.assertEqual(0.11, loan_list[0].loan_amount)
        self.assertEqual(0.0012, loan_list[0].interest_amount)
        self.assertEqual("ethbtc", loan_list[0].symbol)
        self.assertEqual(LoanOrderState.ACCRUAL, loan_list[0].state)
        self.assertEqual(AccountType.SPOT, loan_list[0].account_type)
        self.assertEqual(119910, loan_list[0].user_id)
        self.assertEqual(1511169724000, loan_list[0].accrued_timestamp)
        self.assertEqual(1511169724530, loan_list[0].created_timestamp)
