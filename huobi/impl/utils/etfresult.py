def etf_result_check(code):
    if code == 200:
        return ""
    elif code == 10400:
        return "Invalid ETF name"
    elif code == 13403:
        return "Insufficient asset to create ETF"
    elif code == 13404:
        return "Create and redemption disabled due to system setup"
    elif code == 13405:
        return "Create and redemption disabled due to configuration issue"
    elif code == 13406:
        return "Invalid API call"
    elif code == 13410:
        return "API authentication fails"
    elif code == 13500:
        return "System error"
    elif code == 13601:
        return "Create and redemption disabled during rebalance"
    elif code == 13603:
        return "Create and redemption disabled due to other reason"
    elif code == 13604:
        return "Create suspended"
    elif code == 13605:
        return "Redemption suspended"
    elif code == 13606:
        return "Amount incorrect. For the cases when creation amount or redemption amount is not in the range of min/max amount"
    return ""
