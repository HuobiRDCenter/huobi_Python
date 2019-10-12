class TradeStatisticsSerial:

    @staticmethod
    def json_parse(json_data, ts):
        statistics = TradeStatistics()
        statistics.amount = json_data.get_float("amount")
        statistics.open = json_data.get_float("open")
        statistics.close = json_data.get_float("close")
        statistics.high = json_data.get_float("high")
        statistics.timestamp = ts
        statistics.count = json_data.get_int("count")
        statistics.low = json_data.get_float("low")
        statistics.volume = json_data.get_float("vol")
        return statistics

