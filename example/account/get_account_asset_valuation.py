from huobi.client.account import AccountClient
from huobi.constant import *

account_client = AccountClient(api_key=g_api_key,
                               secret_key=g_secret_key)

account_type = "spot"
asset_valuation = account_client.get_account_asset_valuation(account_type=account_type, valuation_currency="usd")
asset_valuation.print_object()
