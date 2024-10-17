from huobi.model.generic.p import P


class CommonSymbols:

    def __init__(self):
        self.si = ""
        self.scr = ""
        self.sc = ""
        self.dn = ""
        self.bc = ""
        self.bcdn = ""
        self.qc = ""
        self.qcdn = ""
        self.state = ""
        self.whe = None
        self.cd = None
        self.te = None
        self.toa = 0
        self.sp = ""
        self.w = 0
        self.ttp = 0.0
        self.tap = 0.0
        self.tpp = 0.0
        self.fp = 0.0
        self.suspend_desc = ""
        self.transfer_board_desc = ""
        self.tags = ""
        self.lr = 0.0
        self.smlr = 0.0
        self.flr = ""
        self.wr = ""
        self.d = 0
        self.elr = ""
        self.p = []
        self.castate = ""
        self.ca1oa = 0
        self.ca2oa = 0


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.si, format_data + "si")
        PrintBasic.print_basic(self.scr, format_data + "scr")
        PrintBasic.print_basic(self.sc, format_data + "sc")
        PrintBasic.print_basic(self.dn, format_data + "dn")
        PrintBasic.print_basic(self.bc, format_data + "bc")
        PrintBasic.print_basic(self.bcdn, format_data + "bcdn")
        PrintBasic.print_basic(self.qc, format_data + "qc")
        PrintBasic.print_basic(self.qcdn, format_data + "qcdn")
        PrintBasic.print_basic(self.state, format_data + "state")
        PrintBasic.print_basic(self.whe, format_data + "whe")
        PrintBasic.print_basic(self.cd, format_data + "cd")
        PrintBasic.print_basic(self.te, format_data + "te")
        PrintBasic.print_basic(self.toa, format_data + "toa")
        PrintBasic.print_basic(self.sp, format_data + "sp")
        PrintBasic.print_basic(self.w, format_data + "w")
        PrintBasic.print_basic(self.ttp, format_data + "ttp")
        PrintBasic.print_basic(self.tap, format_data + "tap")
        PrintBasic.print_basic(self.tpp, format_data + "tpp")
        PrintBasic.print_basic(self.fp, format_data + "fp")
        PrintBasic.print_basic(self.suspend_desc, format_data + "suspend_desc")
        PrintBasic.print_basic(self.transfer_board_desc, format_data + "transfer_board_desc")
        PrintBasic.print_basic(self.tags, format_data + "tags")
        PrintBasic.print_basic(self.lr, format_data + "lr")
        PrintBasic.print_basic(self.smlr, format_data + "smlr")
        PrintBasic.print_basic(self.flr, format_data + "flr")
        PrintBasic.print_basic(self.wr, format_data + "wr")
        PrintBasic.print_basic(self.d, format_data + "d")
        PrintBasic.print_basic(self.elr, format_data + "elr")
        PrintBasic.print_basic(self.castate, format_data + "castate")
        PrintBasic.print_basic(self.ca1oa, format_data + "ca1oa")
        PrintBasic.print_basic(self.ca2oa, format_data + "ca2oa")
        if self.p and len(self.p):
            for p_obj in self.p:
                p_obj.print_object("\t")
                print()
