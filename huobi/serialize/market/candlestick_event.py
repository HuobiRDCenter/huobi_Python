from huobi.constant import *
from huobi.model.market import *


class CandlestickEventSerial:

    """
    @staticmethod
    def json_parse_adapter(json_wrapper):
        candle_stick_event_obj = CandlestickEventSerial.json_parse(json_wrapper)
        candle_stick_event_obj.interval = interval
        return candle_stick_event_obj
	"""
		
    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelCh)
        parse = ChannelParser(ch)
        candlestick_event = CandlestickEvent()
        candlestick_event.symbol = parse.symbol
        candlestick_event.interval = ""
        candlestick_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
        tick = json_wrapper.get_object(OutputKey.KeyTick)
        data = CandlestickSerial.json_parse(tick)
        candlestick_event.data = data
        return candlestick_event