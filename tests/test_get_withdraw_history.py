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
        "id": 1171,
        "type": "withdraw",
        "currency": "ht",
        "tx-hash": "ed03094b84eafbe4bc16e7ef766ee959885ee5bcb265872baaa9c64e1cf86c2b",
        "amount": 7.457467,
        "address": "rae93V8d2mdoUQHwBDBdM4NHCMehRJAsbm",
        "address-tag": "100040",
        "fee": 345,
        "chain":"aaaa",
        "state": "confirmed",
        "created-at": 1510912472199,
        "updated-at": 1511145876575
      }
    ]
}
'''


class TestGetWithdrawHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User()
        account = Account()
        account.account_type = AccountType.SPOT
        account.id = 12345
        accounts = list()
        accounts.append(account)
        user.accounts = accounts
        account_info_map.user_map["12345"] = user

    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_withdraw_history("btc", 24966984923, 1, "prev")
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/query/deposit-withdraw") != -1)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertTrue(request.url.find("currency=btc") != -1)
        self.assertTrue(request.url.find("from=24966984923") != -1)
        self.assertTrue(request.url.find("size=1") != -1)
        self.assertTrue(request.url.find("type=withdraw") != -1)
        self.assertTrue(request.url.find("direct=prev") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.get_withdraw_history("btc", 24966984923, 1, "prev")
        withdraws = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1, len(withdraws))
        self.assertEqual(345, withdraws[0].fee)
        self.assertEqual(1171, withdraws[0].id)
        self.assertEqual(1510912472199, withdraws[0].created_timestamp)
        self.assertEqual(1511145876575, withdraws[0].updated_timestamp)
        self.assertTrue("rae93V8d2mdoUQHwBDBdM4NHCMehRJAsbm", withdraws[0].address)
        self.assertEqual("100040", withdraws[0].address_tag)
        self.assertEqual("ht", withdraws[0].currency)
        self.assertEqual("ed03094b84eafbe4bc16e7ef766ee959885ee5bcb265872baaa9c64e1cf86c2b", withdraws[0].tx_hash)
        self.assertEqual(WithdrawState.CONFIRMED, withdraws[0].withdraw_state)
