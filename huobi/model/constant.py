class CandlestickInterval:
    MIN1 = "1min"
    MIN5 = "5min"
    MIN15 = "15min"
    MIN30 = "30min"
    MIN60 = "60min"
    HOUR4 = "4hour"
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


class OrderType:
    SELL_LIMIT = "sell-limit"
    BUY_LIMIT = "buy-limit"
    BUY_MARKET = "buy-market"
    SELL_MARKET = "sell-market"
    BUY_IOC = "buy-ioc"
    SELL_IOC = "sell-ioc"
    BUY_LIMIT_MAKER = "buy-limit-maker"
    SELL_LIMIT_MAKER = "sell-limit-maker"
    BUY_STOP_LIMIT = "buy-stop-limit"
    SELL_STOP_LIMIT = "sell-stop-limit"
    BUY_LIMIT_FOK = "buy-limit-fok"
    SELL_LIMIT_FOK = "sell-limit-fok"
    BUY_STOP_LIMIT_FOK = "buy-stop-limit-fok"
    SELL_STOP_LIMIT_FOK = "sell-stop-limit-fok"
    INVALID = None


class AccountType:
    SPOT = "spot"
    MARGIN = "margin"
    OTC = "otc"
    POINT = "point"
    MINEPOLL = "minepool"
    ETF = "etf"
    AGENCY = "agency"
    SUPER_MARGIN = "super-margin"
    INVALID = None


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


class DepositWithdraw:
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


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
    FAILED = "failed"
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
    SUPER_MARGIN_API = "super-margin-api"
    SUPER_MARGIN_WEB = "super-margin-web"
    SUPER_MARGIN_APP = "super-margin-app"
    SUPER_MARGIN_FL_SYS = "super-margin-fl-sys"
    SUPER_MARGIN_FL_MGT = "super-margin-fl-mgt"
    INVALID = None


class OrderState:
    CREATED = "created"   #for stop loss order
    PRE_SUBMITTED = "pre-submitted"
    SUBMITTING = "submitting"
    SUBMITTED = "submitted"
    PARTIAL_FILLED = "partial-filled"
    CANCELLING = "cancelling"
    PARTIAL_CANCELED = "partial-canceled"
    FILLED = "filled"
    CANCELED = "canceled"
    FAILED = "failed"
    PLACE_TIMEOUT = "place_timeout"
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


class AccountBalanceMode:
    BALANCE = "0"
    TOTAL = "1"
    INVALID = None


class OperateMode:
    PING = "ping"
    PONG = "pong"
    INVALID = None


class QueryDirection:
    PREV = "prev"
    NEXT = "next"
    INVALID = None


class TransferFuturesPro:
    TO_PRO = "futures-to-pro"
    TO_FUTURES = "pro-to-futures"


class MatchRole:
    MAKER = "maker"
    TAKER = "taker"


class DepthStep:
    STEP0 = "step0"
    STEP1 = "step1"
    STEP2 = "step2"
    STEP3 = "step3"
    STEP4 = "step4"
    STEP5 = "step5"


class MbpLevel:
    MBP5 = 5
    MBP10 = 10
    MBP20 = 20
    MBP150 = 150


class ChainDepositStatus:
    ALLOWED = "allowed"
    PROHIBITED = "prohibited"
    INVALID = None


class ChainWithdrawStatus:
    ALLOWED = "allowed"
    PROHIBITED = "prohibited"
    INVALID = None


class InstrumentStatus:
    NORMAL = "normal"
    DELISTED = "delisted"
    INVALID = None


class AccountChangeType:
    ORDER_PLACE = "order-place"
    ORDER_MATCH = "order-match"
    ORDER_REFUND = "order-refund"
    ORDER_CANCEL = "order-cancel"
    ORDER_FEE_REFUND = "order-fee-refund"
    MARGIN_TRANSFER = "margin-transfer"
    MARGIN_LOAN = "margin-loan"
    MARGIN_INTEREST = "margin-interest"
    MARGIN_REPAY = "margin-repay"
    OTHER = "other"
    INVALID = None


class FeeDeductType:
    DEDUCT_BY_HT = "ht"
    DEDUCT_BY_POINT = "point"
    INVALID = None


class SubUidState:
    UNLOCK = "unlock"
    LOCK = "lock"
    INVALID = None


class OrderUpdateEventType:
    CREATION = "creation"
    TRADE = "trade"
    CANCELLATION = "cancellation"
    INVALID = None
