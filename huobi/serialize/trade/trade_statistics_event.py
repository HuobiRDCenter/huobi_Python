from huobi.utils.channelparser import ChannelParser
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model.tradestatistics import TradeStatistics


class TradeStatisticsEventSerial:

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string("ch")
        parse = ChannelParser(ch)
        trade_statistics_event = TradeStatisticsEvent()
        trade_statistics_event.symbol = parse.symbol
        ts = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
        trade_statistics_event.timestamp = ts
        tick = json_wrapper.get_object("tick")
        statistics = TradeStatistics.json_parse(tick, ts)
        trade_statistics_event.trade_statistics = statistics
        return trade_statistics_event


