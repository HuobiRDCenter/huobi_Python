import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map


data = '''
{
       "status": "ok",
    "data": [
    {
       "id": 9910049,
       "type": "spot",
       "list": [
             {
           "currency": "btc",
            "type": "trade",
            "balance": "1.00"
         },
         {
           "currency": "eth",
           "type": "trade",
           "balance": "1934.00"
         }
         ]
    },
    {
    "id": 9910050,
    "type": "point",
    "list": []
    }
    ]
}
'''


class TestGetSpecifyAccount(unittest.TestCase):

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_specify_account_balance(12345)
        path = "/v1/account/accounts/{}"
        path = path.format(12345)
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find(path) != -1)
        self.assertTrue(request.url.find("Signature") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_specify_account_balance(12345)
        complete_sub_account_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(complete_sub_account_list))
        self.assertEqual(9910049, complete_sub_account_list[0].id)
        self.assertEqual(AccountType.SPOT, complete_sub_account_list[0].account_type)
        self.assertEqual(9910050, complete_sub_account_list[1].id)

        self.assertEqual(AccountType.POINT, complete_sub_account_list[1].account_type)
        self.assertEqual("btc", complete_sub_account_list[0].balances[0].currency)
        self.assertEqual(BalanceType.TRADE, complete_sub_account_list[0].balances[0].type)
        self.assertEqual(1, complete_sub_account_list[0].balances[0].balance)
        self.assertEqual("eth", complete_sub_account_list[0].balances[1].currency)
        self.assertEqual(BalanceType.TRADE, complete_sub_account_list[0].balances[1].type)
        self.assertEqual(1934, complete_sub_account_list[0].balances[1].balance)
        self.assertEqual(0, len(complete_sub_account_list[1].balances))
        self.assertEqual(2, len(complete_sub_account_list[0].balances))
