class CandlestickInterval:
    MIN1 = "1min"
    MIN5 = "5min"
    MIN15 = "15min"
    MIN30 = "30min"
    MIN60 = "60min"
    DAY1 = "1day"
    MON1 = "1mon"
    WEEK1 = "1week"
    YEAR1 = "1year"
    INVALID = None


class OrderSide:
    BUY = "buy"
    SELL = "sell"
    INVALID = None


class TradeDirection:
    BUY = "buy"
    SELL = "sell"
    INVALID = None


class TradeOffset:
    OPEN = "open"
    CLOSE = "close"
    INVALID = None


class OrderType:
    SELL_LIMIT = "sell-limit"
    BUY_LIMIT = "buy-limit"
    BUY_MARKET = "buy-market"
    SELL_MARKET = "sell-market"
    BUY_IOC = "buy-ioc"
    SELL_IOC = "sell-ioc"
    BUY_LIMIT_MAKER = "buy-limit-maker"
    SELL_LIMIT_MAKER = "sell-limit-maker"
    INVALID = None


class AccountType:
    SPOT = "spot"
    MARGIN = "margin"
    OTC = "otc"
    POINT = "point"
    INVALID = None

class ContractType:
    """
    合约类型 ("this_week":当周 "next_week":下周 "quarter":季度)
    """
    THIS_WEEK = "this_week"
    NEXT_WEEK = "next_week"
    QUARTER = "quarter"





class AccountState:
    WORKING = "working"
    LOCK = "lock"
    INVALID = None


class BalanceType:
    TRADE = "trade"
    FROZEN = "frozen"
    LOAN = "loan"
    INTEREST = "interest"
    LOAN_AVAILABLE = "loan-available"
    TRANSFER_OUT_AVAILABLE = "transfer-out-available"
    INVALID = None


class WithdrawState:
    SUBMITTED = "submitted"
    REEXAMINE = "reexamine"
    CANCELED = "canceled"
    PASS = "pass"
    REJECT = "reject"
    PRETRANSFER = "pre-transfer"
    WALLETTRANSFER = "wallet-transfer"
    WALEETREJECT = "wallet-reject"
    CONFIRMED = "confirmed"
    CONFIRMERROR = "confirm-error"
    REPEALED = "repealed"
    INVALID = None


class DepositState:
    CONFIRMING = "confirming"
    SAFE = "safe"
    CONFIRMED = "confirmed"
    ORPHAN = "orphan"
    INVALID = None


class LoanOrderState:
    CREATED = "created"
    ACCRUAL = "accrual"
    CLEARED = "cleared"
    INVALID = None


class OrderSource:
    SYS = "sys"
    WEB = "web"
    API = "api"
    APP = "app"
    FL_SYS = "fl-sys"
    FL_MGT = "fl-mgt"
    SPOT_WEB = "spot-web"
    SPOT_API = "spot-api"
    SPOT_APP = "spot-app"
    MARGIN_API = "margin-api"
    MARGIN_WEB = "margin-web"
    MARGIN_APP = "margin-app"
    INVALID = None


class OrderState:
    SUBMITTED = "submitted"
    PARTIAL_FILLED = "partial-filled"
    CANCELLING = "cancelling"
    PARTIAL_CANCELED = "partial-canceled"
    FILLED = "filled"
    CANCELED = "canceled"
    INVALID = None


class TransferMasterType:
    IN = "master-transfer-in"
    OUT = "master-transfer-out"
    POINT_IN = "master-point-transfer-in"
    POINT_OUT = "master-point-transfer-out"
    INVALID = None


class EtfStatus:
    NORMAL = "1"
    REBALANCING_START = "2"
    CREATION_AND_REDEMPTION_SUSPEND = "3"
    CREATION_SUSPEND = "4"
    REDEMPTION_SUSPEND = "5"
    INVALID = None


class EtfSwapType:
    IN = "1"
    OUT = "2"
    INVALID = None


class AccountChangeType:
    NEWORDER = "order.place"
    TRADE = "order.match"
    REFUND = "order.refund"
    CANCELORDER = "order.cancel"
    FEE = "order.fee-refund"
    TRANSFER = "margin.transfer"
    LOAN = "margin.loan"
    INTEREST = "margin.interest"
    REPAY = "margin.repay"
    OTHER = "other"
    INVALID = None


class BalanceMode:
    AVAILABLE = "0"
    TOTAL = "1"
    INVALID = None


class QueryDirection:
    PREV = "prev"
    NEXT = "next"
    INVALID = None

