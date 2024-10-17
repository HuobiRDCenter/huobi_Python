from huobi.client.generic import GenericClient


"""
GET https://status.huobigroup.com/api/v2/summary.json
"""
generic_client = GenericClient()
system_status = generic_client.get_system_status()
print(system_status)



