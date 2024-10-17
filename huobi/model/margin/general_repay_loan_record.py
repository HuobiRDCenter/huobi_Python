from huobi.constant import *


class GeneralRepayLoanRecord:
    """
    The general repay loan record information.

    :member
        repayId: repayment transaction ID.
        repayTime: repayment transaction time (unix time in millisecond).
        accountId: repayment account ID.
        currency: repayment currency, like "usdt".
        repaidAmount: repaid amount.
        transactIds: ID list of original loan transactions (arranged by order of repayment time).
        nextId: search the start ID in the next page (return only when there is data in the next page).
    """

    def __init__(self):
        self.repayId = None
        self.repayTime = None
        self.accountId = None
        self.currency = None
        self.repaidAmount = None
        self.transactIds = Transact()
        self.nextId = None

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.repayId, format_data + "repayId")
        PrintBasic.print_basic(self.repayTime, format_data + "repayTime")
        PrintBasic.print_basic(self.accountId, format_data + "accountId")
        PrintBasic.print_basic(self.currency, format_data + "currency")
        PrintBasic.print_basic(self.repaidAmount, format_data + "repaidAmount")
        PrintBasic.print_basic(self.transactIds, format_data + "transactIds")
        PrintBasic.print_basic(self.nextId, format_data + "nextId")

        print()


class Transact:

    """
    The general repay loan record information.

    :member
        transactId: original loan transaction ID.
        repaidPrincipal: principal repaid.
        repaidInterest: interest repaid.
        paidHt: HT paid.
        paidPoint: point paid.
    """

    def __init__(self):
        self.transactId = None
        self.repaidPrincipal = None
        self.repaidInterest = None
        self.paidHt = None
        self.paidPoint = None

