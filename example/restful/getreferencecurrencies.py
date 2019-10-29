from huobi import RequestClient


client = RequestClient()

list_obj = client.get_reference_currencies()
if len(list_obj):
    for reference_currency in list_obj:
        reference_currency.print_object()


list_obj = client.get_reference_currencies(currency="usdt")
if len(list_obj):
    for reference_currency in list_obj:
        reference_currency.print_object()
