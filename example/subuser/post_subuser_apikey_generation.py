from huobi.client.subuser import SubuserClient
from huobi.constant import *

subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)

otp_token = '746316'
sub_uid = 122946475
note = "huobi_subuser"
permission = 'readOnly'
# ip_addresses = ''

result = subuser_client.post_subuser_apikey_generate(otp_token, sub_uid, note, permission)
result.print_object()
