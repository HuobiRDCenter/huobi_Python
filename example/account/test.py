
import requests
import json

url = "https://linear-api.global-test-23.tc-jp1.huobiapps.com/linear-swap-api/v1/swap_cross_order"

payload = json.dumps({
  "contract_code": "BTC-USDT",
  "direction": "buy",
  "offset": "both",
  "price": 0.16,
  "lever_rate": 5,
  "volume": 1,
  "order_price_type": "limit"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)