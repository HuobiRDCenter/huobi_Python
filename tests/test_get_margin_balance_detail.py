import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
	"status": "ok",
	"data": [{
		"id": 6725534,
		"type": "margin",
		"state": "working",
		"symbol": "btcusdt",
		"fl-price": "0",
		"fl-type": "safe",
		"risk-rate": "10",
		"list": [{
			"currency": "btc",
			"type": "trade",
			"balance": "0"
		}, {
			"currency": "btc",
			"type": "frozen",
			"balance": "0"
		}, {
			"currency": "btc",
			"type": "loan",
			"balance": "0"
		}, {
			"currency": "btc",
			"type": "interest",
			"balance": "0"
		}, {
			"currency": "usdt",
			"type": "trade",
			"balance": "3"
		}, {
			"currency": "usdt",
			"type": "frozen",
			"balance": "0"
		}, {
			"currency": "usdt",
			"type": "loan",
			"balance": "0"
		}, {
			"currency": "usdt",
			"type": "interest",
			"balance": "0"
		}, {
			"currency": "btc",
			"type": "transfer-out-available",
			"balance": "0"
		}, {
			"currency": "usdt",
			"type": "transfer-out-available",
			"balance": "3"
		}, {
			"currency": "btc",
			"type": "loan-available",
			"balance": "0"
		}, {
			"currency": "usdt",
			"type": "loan-available",
			"balance": "0"
		}]
	}]
}
'''

class TestGetMarginBalanceDetail(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_margin_balance_detail("htbtc",123)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/margin/accounts/balance") != -1)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("symbol=htbtc") != -1)
        self.assertTrue(request.url.find("symbol=htbtc") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_margin_balance_detail("htbtc", 123)
        margin_balance_detail_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1, len(margin_balance_detail_list))
        self.assertEqual(12, len(margin_balance_detail_list[0].sub_account_balance_list))
        self.assertEqual(6725534, margin_balance_detail_list[0].id)
        self.assertEqual(AccountType.MARGIN, margin_balance_detail_list[0].type)
        self.assertEqual(AccountState.WORKING, margin_balance_detail_list[0].state)
        self.assertEqual("btcusdt", margin_balance_detail_list[0].symbol)
        self.assertEqual(0, margin_balance_detail_list[0].fl_price)
        self.assertEqual("safe", margin_balance_detail_list[0].fl_type)
        self.assertEqual(10, margin_balance_detail_list[0].risk_rate)
        self.assertEqual("usdt", margin_balance_detail_list[0].sub_account_balance_list[4].currency)
        self.assertEqual(BalanceType.TRADE, margin_balance_detail_list[0].sub_account_balance_list[4].balance_type)
        self.assertEqual(3, margin_balance_detail_list[0].sub_account_balance_list[4].balance)
