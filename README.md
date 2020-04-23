# Huobi Python SDK

This is Huobi Python SDK, This is a lightweight python library, you can import to your python project and use this SDK to query all market data, trading and manage your account.

The SDK supports both synchronous RESTful API invoking, and subscribe the market data from the Websocket connection.

## Huobi Python SDK Releases

Go to [Releases](https://github.com/HuobiRDCenter/huobi_Python/releases) page to view and download each release.


## Table of Contents

- [Beginning](#Beginning)
  - [Installation](#Installation)
  - [Quick Start](#Quick-Start)
  - [Request vs. Subscription](#Request-vs.-Subscription)
  - [Clients](#Clients)
  - [Create client](#create-client)
  - [Custom host](#custom-host)
- [Usage](#Usage)

  - [Request](#Request)
  - [Subscription](#Subscription)
  - [Error handling](#error-handling)
- [Request example](#Request-example)

  - [Reference data](#Reference-data)
    - [Exchange timestamp](#Exchange-timestamp)
    - [Symbol and currencies](#symbol-and-currencies)
  - [Market data](#Market-data)
    - [Candlestick/KLine](#Candlestick/KLine)
    - [Depth](#Depth)
    - [Latest trade](#latest-trade)
    - [Best bid/ask](#best-bid/ask)
    - [Historical](#historical)
    - [24H Statistics](#24h-statistics)
  - [Account](#account)
  - [Wallet](#wallet)
    - [Withdraw](@Withdraw)
    - [Cancel withdraw](@cancel-withdraw)
    - [Withdraw and deposit history](#withdraw-and-deposit-history)
  - [Trading](#trading)
    - [Create order](#create-order)
    - [Cancel order](#cancel-order)
    - [Cancel open orders](#cancel-open-orders)
    - [Get order info](#get-order-info)
  - [Margin Loan](#margin-loan)
    - [Apply loan](#apply-loan)
    - [Reply loan](#reply-loan)
    - [Loan history](#loan-history)
- [Subscription example](#Subscription-example)
  - [Implement the listener](#Implement-the0listener)
  - [Subscribe market data](#Subscribe-market-data)
  - [Subscribe order update](#subscribe-order-update)
  - [Subscribe account change](#subscribe-account-change)
  - [Unsubscribe](#unsubscribe)

  

## Beginning

### Installation

*The SDK is compiled by Python 3.7 and above*

#### Pip

*The pip installation will be supported in final version.*

For Beta version, please import the source code directly.

The example code is in python3/example.



To install by source code, run below command

```python
python3 setup.py install
```



### Quick Start

In your python project, you can follow below steps:

* Create the client instance.
* Call the interfaces provided by client.

```python
request_client = RequestClient()

# Get the timestamp from Huobi server and print on console
timestamp = request_client.get_exchange_timestamp
print(timestamp)

# Get the latest btcusdt‘s candlestick data and print the highest price on console
candlestick_list = request_client.get_latest_candlestick("btcusdt", CandlestickInterval.DAY1, 20)
for item in candlestick_list:
    print(item.high)
```

Please NOTE:

All timestamp which is got from SDK is the Unix timestamp based on UTC.



### Request vs. Subscription

Huobi API supports 2 types of invoking.

1. Request method: You can use request method to trade, withdraw and loan. You can also use it to get the market related data from Huobi server.
2. Subscription method: You can subscribe the market updated data and account change from Huobi server. For example, if you subscribed the price depth update, you will receive the price depth message when the price depth updates on Huobi server.

We recommend developers to use request method to trade, withdraw and loan, to use subscription method to access the market related data.



### Clients

There are 2 clients, one is for request method, ```RequestClient``` , another is for subscription method ```SubscriptionClient```. 

* **RequestClient**: It is a synchronous request, it will invoke the Huobi API via synchronous method, all invoking will be blocked until receiving the response from server.

* **SubscriptionClient**: It is the subscription, it is used for subscribing any market data update and account change.  It is asynchronous, so you must implement  ```callback()``` function. The server will push any update for the client. if client receive the update, the ```callback()``` function will be called. See [Subscription usage](#Subscription) for detail. 

  

### Create client

You can assign the API key and Secret key when you create the client. See below:

```python
request_client = RequestClient(api_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", secret_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx")
```

```python
subscription_client = SubscriptionClient(api_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", secret_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx")
```

The API key and Secret key are used for authentication.

Some APIs related with account, trading, deposit and withdraw etc require the authentication. We can name them after private interface.

The APIs only return the market data that don't need the authentication. We can name them after public interface.

If you want to invoke both public interface and private interface. You must apply API Key and Secret Key from Huobi and put them into the client you created.

If the authentication cannot pass, the invoking of private interface will fail.

If you want to invoke public interface only. You can create the client as follow:

```python
request_client = RequestClient()
```

```python
subscription_client = SubscriptionClient()
```



### Custom host

To support huobi cloud, you can specify the custom host.

1. Set your custom host to ```RequestClient``` or ```SubscriptionClient```.
2. Set the url or uri string to client when creating the client instance.

See below example

```python
# Set custom host for request
request_client = RequestClient(api_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", secret_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", url="https://www.xxx.yyy/")


# Set custom host for subscription
subscription_client = SubscriptionClient(api_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", secret_key="xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxx", uri="wss://www.xxx.yyy")
```

If you do not set yout custom host, below default host will be used:

For request: https://api.huobi.pro

For subscription: wss://api.huobi.pro



## Usage

### Request

To invoke the interface by synchronous, you can create the ```RequestClient``` and call the API directly.

```python
request_client = RequestClient()
# Get the best bid and ask for btcusdt, print the best ask price and amount on console.
best_quote = request_client.get_best_quote("btcusdt")
print(best_quote.ask_price)
print(best_quote.ask_amount)
```



### Subscription

To receive the subscribed data, you can create the ```SubscriptionClient```. When subscribing the event, you should define your callback function. See below example:

```python
subscription_client = SubscriptionClient()

# Subscribe the trade update for btcusdt.
def callback(trade_event: 'TradeEvent'):
    print(trade_event.symbol)
    for trade in trade_event.trade_list:
        print(trade.price)

subscription_client.subscribe_trade_event("btcusdt", callback)
```

The subscription method supports multi-symbol string. Each symbol should be separated by a comma.

```python
subscription_client.subscribe_trade_event("btcusdt,ethusdt", callback)
```



### Error handling

#### For request

In error case, such as you set the invalid symbol to ```get_best_quote()```. The ```HuobiApiException``` will be thrown. See below example:

```python
try:
    best_quote = request_client.get_best_quote("abcdefg")
    print(best_quote.ask_price)
    print(best_quote.ask_amount)
except HuobiApiException as e:
    print(e.error_code)
    print(e.error_message)

```

#### For Subscription

If you want to check the error, you should implement your ```error_handler```. See below example:

```python
def callback(trade_event: 'TradeEvent'):
    print(trade_event.symbol)
    for trade in trade_event.trade_list:
        print(trade.price)

def error_handler(e: 'HuobiApiException'):
    print(e.error_code)
    print(e.error_message)

subscription_client.subscribe_trade_event("abcdefg", callback, error_handler)
```

Any error made during subscription will be output to a log file, If you do not define your ```error_handler```, the error will be output to log only.

#### Error log

The SDK is using the common logging module, to show it to console, you can follow below steps before create the client:

```python
logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
```



## Request example

### Reference data

#### Exchange timestamp

```python
//Synchronous
timestamp = request_client.get_exchange_timestamp()
print(timestamp)
```

#### Symbol and currencies

```python
exchange_info = request_client.get_exchange_info()
for currency in exchange_info.currencies:
    print(currency)
```

### Market data

#### Candlestick/KLine

```python
candlestick_list = request_client.get_latest_candlestick("btcusdt", CandlestickInterval.DAY1, 20)
for candlestick in candlestick_list:
    print(candlestick.high)
```

#### Depth

```python
price_depth = request_client.get_price_depth("btcusdt", 5)
for depth in price_depth.bids:
    print(depth.price)
```

#### Latest trade

```python
trade = request_client.get_last_trade("btcusdt")
print(trade.price)
```

#### Best bid/ask

```python
best_quote = request_client.get_best_quote("btcusdt")
print(best_quote.ask_price)
print(best_quote.ask_amount)
```

#### Historical

```python
trade_list = request_client.get_historical_trade("btcusdt", 5)
print(trade_list[0].price)
```

#### 24H statistics

```python
trade_statistics = request_client.get_24h_trade_statistics("btcusdt")
print(trade_statistics.open)
```

### Account

*Authentication is required.*

```python
balance = request_client.get_account_balance_by_account_type(AccountType.SPOT)
print(balance.get(0).get(0).balance)
```

### Wallet

#### Withdraw

*Authentication is required.*

```python
id = request_client.withdraw("xxxxxxx", 0.1, "btc")
print(id)
```

#### Cancel withdraw

*Authentication is required.*

```python
request_client.cancel_withdraw("btc", id)
```

#### Withdraw and deposit history

*Authentication is required.*

```python
withdraw_list = request_client.get_withdraw_history("btc", id, 10)
print(withdraw_list[0].amount)
deposit_list = request_client.get_deposit_history("btc", id, 10)
print(deposit_list[0].amount)
```

### Trading

#### Create order

*Authentication is required.*

```python
order_id = request_client.create_order("btcusdt", AccountType.SPOT, OrderType.BUY_LIMIT, 1.0, 1.0)
print(id)
```

#### Cancel order

*Authentication is required.*

```python
request_client.cancel_order("btcusdt", order_id)
```

#### Cancel open orders

*Authentication is required.*

```python
result = request_client.cancel_open_orders("btcusdt", AccountType.SPOT, OrderSide.SELL, 10)
print(result.success_count)
```

#### Get order info

*Authentication is required.*

```python
order = request_client.get_order("symbol", id)
print(order.price)
```

#### Historical orders

*Authentication is required.*

```python
order_list = request_client.get_historical_orders("symbol", OrderState.SUBMITTED)
print(order_list[0].price)
```

### Margin Loan

####Apply loan

*Authentication is required.*

```python
id = request_client.apply_loan("btcusdt", "btc", 10.0)
print(id)
```

#### Repay loan

*Authentication is required.*

```python
id = request_client.repay_loan(id, 10.0)
print(id)
```

####Loan history

*Authentication is required.*

```python
loan_list = request_client.get_loan_history("btcusdt")
print(loan_list[0].loan_amount)
```



## Subscription example

### Subscribe trade update

```python
def callback(trade_event: 'TradeEvent'):
    print(trade_event.symbol)
    for trade in trade_event.trade_list:
        print(trade.price)

subscription_client.subscribe_trade_event("btcusdt", callback)
```

###Subscribe candlestick/KLine update

```python
def callback(candlestick_event: 'CandlestickEvent'):
    print(candlestick_event.data.high)

subscription_client.subscribe_candlestick_event("btcusdt", CandlestickInterval.MIN15, callback)
```

### Subscribe orders update

*Authentication is required.*

```python
def callback(orders_update_event: 'OrdersUpdateEvent'):
    orders_update_event.print_object()

subscription_client.subscribe_orders_update_event("btcusdt", callback)
```

### Subscribe account change

*Authentication is required.*

```python
def callback(account_event: 'AccountsUpdateEvent'):
    account_event.print_object()

subscription_client.subscribe_accounts_update_event(AccountBalanceMode.TOTAL, callback)
```

### Unsubscribe

You can cancel all subscription by calling ```unsubscribe_all()```.

```python
subscription_client.unsubscribe_all()
```


