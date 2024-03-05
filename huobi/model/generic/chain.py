from huobi.constant import *

class Chain:
    """
    The Huobi Chain.

    :member
        chain: Chain name
        numOfConfirmations: Number of confirmations required for deposit success (trading & withdrawal allowed once reached)
        numOfFastConfirmations: Number of confirmations required for quick success (trading allowed but withdrawal disallowed once reached)
        minDepositAmt: Minimal deposit amount in each request
        depositStatus: Deposit status	allowed,prohibited
        minWithdrawAmt: Minimal withdraw amount in each request.
        maxWithdrawAmt : Maximum withdraw amount in each request
        withdrawQuotaPerDay : Maximum withdraw amount in a day
        withdrawQuotaPerYear : Maximum withdraw amount in a year
        withdrawQuotaTotal : Maximum withdraw amount in total
        withdrawPrecision : Withdraw amount precision
        withdrawFeeType : Type of withdraw fee (only one type can be applied to each currency)

        transactFeeWithdraw : Withdraw fee in each request (only applicable to withdrawFeeType = fixed)
        minTransactFeeWithdraw : Minimal withdraw fee in each request (only applicable to withdrawFeeType = circulated)
        maxTransactFeeWithdraw : Maximum withdraw fee in each request (only applicable to withdrawFeeType = circulated or ratio)
        transactFeeRateWithdraw : Withdraw fee in each request (only applicable to withdrawFeeType = ratio)
        withdrawStatus : Withdraw status
    """

    def __init__(self):
        self.chain = ""
        self.baseChain = ""
        self.baseChainProtocol = ""
        self.numOfConfirmations = 0
        self.numOfFastConfirmations = 0
        self.depositStatus = ChainDepositStatus.INVALID
        self.minDepositAmt = 0
        self.withdrawStatus = ChainWithdrawStatus.INVALID
        self.minWithdrawAmt = 0
        self.withdrawPrecision = 0
        self.maxWithdrawAmt = 0.0
        self.withdrawQuotaPerDay = 0.0
        self.withdrawQuotaPerYear = 0.0
        self.withdrawQuotaTotal = 0.0
        self.withdrawFeeType = ""
        self.transactFeeWithdraw = 0.0
        self.minTransactFeeWithdraw = 0.0
        self.maxTransactFeeWithdraw = 0.0
        self.transactFeeRateWithdraw = 0.0
        self.displayName = ""
        self.isDynamic = None

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.chain, format_data + "Chain")
        PrintBasic.print_basic(self.baseChain, format_data + "Base Chain")
        PrintBasic.print_basic(self.baseChainProtocol, format_data + "Base Chain Protocol")
        PrintBasic.print_basic(self.numOfConfirmations, format_data + "numOfConfirmations")
        PrintBasic.print_basic(self.numOfFastConfirmations, format_data + "numOfFastConfirmations")
        PrintBasic.print_basic(self.depositStatus, format_data + "depositStatus")
        PrintBasic.print_basic(self.minDepositAmt, format_data + "minDepositAmount")
        PrintBasic.print_basic(self.withdrawStatus, format_data + "withdrawStatus")
        PrintBasic.print_basic(self.minWithdrawAmt, format_data + "minWithdrawAmount")
        PrintBasic.print_basic(self.withdrawPrecision, format_data + "withdrawPrecision")
        PrintBasic.print_basic(self.maxWithdrawAmt, format_data + "maxWithdrawAmount")
        PrintBasic.print_basic(self.withdrawQuotaPerDay, format_data + "withdrawQuotaPerDay")
        PrintBasic.print_basic(self.withdrawQuotaPerYear, format_data + "withdrawQuotaPerYear")
        PrintBasic.print_basic(self.withdrawQuotaTotal, format_data + "withdrawQuotaTotal")
        PrintBasic.print_basic(self.withdrawFeeType, format_data + "withdrawFeeType")
        PrintBasic.print_basic(self.transactFeeWithdraw, format_data + "transactFeeWithdraw")
        PrintBasic.print_basic(self.minTransactFeeWithdraw, format_data + "minTransactFeeWithdraw")
        PrintBasic.print_basic(self.maxTransactFeeWithdraw, format_data + "maxTransactFeeWithdraw")
        PrintBasic.print_basic(self.transactFeeRateWithdraw, format_data + "transactFeeRateWithdraw")
