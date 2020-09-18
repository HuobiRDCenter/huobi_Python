from huobi.utils.print_mix_object import *


def key_trans(key_origin):
    if key_origin and len(key_origin) > 1:
        return key_origin.replace("-", "_")
    else:
        return ""


def fill_obj(dict_data, class_name=object):
    obj = class_name()
    for ks, vs in dict_data.items():
        obj_key = key_trans(ks)
        # print("===== fill_obj =====", ks, obj_key, str(vs))
        if hasattr(obj, obj_key):
            setattr(obj, obj_key, vs)
            continue
    return obj


def fill_obj_list(list_data, class_name):
    if (TypeCheck.is_list(list_data)):
        inner_obj_list = list()
        for idx, row in enumerate(list_data):
            inner_obj = fill_obj(row, class_name)
            inner_obj_list.append(inner_obj)
        return inner_obj_list

    return list()


def default_parse(dict_data, outer_class_name=object, inner_class_name=object):
    from huobi.utils.print_mix_object import TypeCheck
    rsp_obj = outer_class_name()

    for outer_key, outer_value in dict_data.items():
        obj_key = key_trans(outer_key)
        # print("===", outer_key, obj_key, str(outer_value))
        # PrintBasic.print_basic_bool(hasattr(rsp_obj, obj_key))
        if hasattr(rsp_obj, obj_key):
            new_value = outer_value
            # print("==========", type(outer_value), outer_value)
            if (TypeCheck.is_list(outer_value)):
                new_value = fill_obj_list(outer_value, inner_class_name)
            elif (TypeCheck.is_dict(outer_value)):
                new_value = fill_obj(outer_value, inner_class_name)

            setattr(rsp_obj, obj_key, new_value)
            continue

    return rsp_obj


def default_parse_data_as_long(ret_original_json, key_name=None, default_value=0):
    if ret_original_json:
        # from data get value by key_name
        if key_name and len(key_name):
            data_json = ret_original_json.get("data", {})
            ret_val = data_json.get(key_name, default_value)
        else:
            # get data value
            ret_val = ret_original_json.get("data", 0)
        return None if ret_val is None else int(ret_val)
    else:
        return default_value


def default_parse_list_dict(inner_data, inner_class_name=object, default_value=None):
    from huobi.utils.print_mix_object import TypeCheck

    new_value = default_value
    if inner_data and len(inner_data):
        if (TypeCheck.is_list(inner_data)):
            new_value = fill_obj_list(inner_data, inner_class_name)
        elif (TypeCheck.is_dict(inner_data)):
            new_value = fill_obj(inner_data, inner_class_name)
        else:
            new_value = default_value

    return new_value


def default_parse_fill_directly(dict_data, outer_class_name=object):
    rsp_obj = outer_class_name()

    for outer_key, outer_value in dict_data.items():
        obj_key = key_trans(outer_key)
        if hasattr(rsp_obj, obj_key):
            new_value = outer_value
            setattr(rsp_obj, obj_key, new_value)
            continue

    return rsp_obj


if __name__ == "__main__":
    # json_str = """{"id":1571037900,"open":8306.850000000000000000,"close":8307.990000000000000000,"low":8305.800000000000000000,"high":8308.000000000000000000,"amount":4.314954363225502510,"vol":35845.853207199999993966820000000000000000,"count":45}"""
    # obj = parse(json_str, outer_class_name=Candlestick, inner_class_name=None)

    # obj.print_object()

    # json_str = """{"status":"ok","ch":"market.btcusdt.kline.1min","ts":1571038189274,"data":[{"id":1571038140,"open":8304.130000000000000000,"close":8305.000000000000000000,"low":8300.010000000000000000,"high":8305.000000000000000000,"amount":41.791380418639796061,"vol":347038.873910589999990613890000000000000000,"count":165},{"id":1571038080,"open":8306.060000000000000000,"close":8304.130000000000000000,"low":8304.130000000000000000,"high":8306.060000000000000000,"amount":3.440305012281757977,"vol":28571.704804969999998985000000000000000000,"count":70},{"id":1571038020,"open":8303.890000000000000000,"close":8305.990000000000000000,"low":8303.890000000000000000,"high":8307.000000000000000000,"amount":6.164746957847080072,"vol":51200.094613737306439860000000000000000000,"count":89},{"id":1571037960,"open":8308.000000000000000000,"close":8303.660000000000000000,"low":8303.610000000000000000,"high":8308.430000000000000000,"amount":9.449641840557003640,"vol":78488.394246429999983963200000000000000000,"count":128},{"id":1571037900,"open":8306.850000000000000000,"close":8307.990000000000000000,"low":8305.800000000000000000,"high":8308.000000000000000000,"amount":4.314954363225502510,"vol":35845.853207199999993966820000000000000000,"count":45},{"id":1571037840,"open":8305.290000000000000000,"close":8306.820000000000000000,"low":8305.040000000000000000,"high":8307.300000000000000000,"amount":3.661411574656800047,"vol":30412.286333819999984471300000000000000000,"count":68},{"id":1571037780,"open":8306.500000000000000000,"close":8305.490000000000000000,"low":8305.100000000000000000,"high":8307.690000000000000000,"amount":2.958112866447550895,"vol":24569.573928609999984901150000000000000000,"count":59},{"id":1571037720,"open":8306.300000000000000000,"close":8307.560000000000000000,"low":8305.440000000000000000,"high":8309.000000000000000000,"amount":8.506926000000000000,"vol":70665.848347860000000000000000000000000000,"count":90},{"id":1571037660,"open":8306.920000000000000000,"close":8306.300000000000000000,"low":8306.200000000000000000,"high":8307.000000000000000000,"amount":5.084311000000000000,"vol":42233.572201310000000000000000000000000000,"count":57},{"id":1571037600,"open":8307.200000000000000000,"close":8306.920000000000000000,"low":8306.920000000000000000,"high":8309.160000000000000000,"amount":4.540090141728746275,"vol":37715.585646199999989163880000000000000000,"count":54}]}"""
    # obj_event = parse(json_str, outer_class_name=CandlestickRsp, inner_class_name=Candlestick)
    # obj_event.print_object()

    # json_str = """{"status":"ok","ch":"market.btcusdt.kline.1min","ts":1571038189274,"data":{"id":1571038140,"open":8304.130000000000000000,"close":8305.000000000000000000,"low":8300.010000000000000000,"high":8305.000000000000000000,"amount":41.791380418639796061,"vol":347038.873910589999990613890000000000000000,"count":165}}"""
    # obj_event = parse(json_str, outer_class_name=CandlestickEvent, inner_class_name=Candlestick)
    # obj_event.print_object()

    # json_str = """{"status":"ok","ch":"market.btcusdt.kline.1min","ts":1571038189274,"data":{"id":1571038140,"open":8304.130000000000000000,"close":8305.000000000000000000,"low":8300.010000000000000000,"high":8305.000000000000000000,"amount":41.791380418639796061,"vol":347038.873910589999990613890000000000000000,"count":165}}"""
    # ret = default_parse_restful(json_str, inner_class_name=Candlestick, default_value=None)
    # ret.print_object()

    # json_str = """{"status":"ok","ch":"market.btcusdt.kline.1min","ts":1571038189274,"data":[{"id":1571038140,"open":8304.130000000000000000,"close":8305.000000000000000000,"low":8300.010000000000000000,"high":8305.000000000000000000,"amount":41.791380418639796061,"vol":347038.873910589999990613890000000000000000,"count":165},{"id":1571038080,"open":8306.060000000000000000,"close":8304.130000000000000000,"low":8304.130000000000000000,"high":8306.060000000000000000,"amount":3.440305012281757977,"vol":28571.704804969999998985000000000000000000,"count":70},{"id":1571038020,"open":8303.890000000000000000,"close":8305.990000000000000000,"low":8303.890000000000000000,"high":8307.000000000000000000,"amount":6.164746957847080072,"vol":51200.094613737306439860000000000000000000,"count":89},{"id":1571037960,"open":8308.000000000000000000,"close":8303.660000000000000000,"low":8303.610000000000000000,"high":8308.430000000000000000,"amount":9.449641840557003640,"vol":78488.394246429999983963200000000000000000,"count":128},{"id":1571037900,"open":8306.850000000000000000,"close":8307.990000000000000000,"low":8305.800000000000000000,"high":8308.000000000000000000,"amount":4.314954363225502510,"vol":35845.853207199999993966820000000000000000,"count":45},{"id":1571037840,"open":8305.290000000000000000,"close":8306.820000000000000000,"low":8305.040000000000000000,"high":8307.300000000000000000,"amount":3.661411574656800047,"vol":30412.286333819999984471300000000000000000,"count":68},{"id":1571037780,"open":8306.500000000000000000,"close":8305.490000000000000000,"low":8305.100000000000000000,"high":8307.690000000000000000,"amount":2.958112866447550895,"vol":24569.573928609999984901150000000000000000,"count":59},{"id":1571037720,"open":8306.300000000000000000,"close":8307.560000000000000000,"low":8305.440000000000000000,"high":8309.000000000000000000,"amount":8.506926000000000000,"vol":70665.848347860000000000000000000000000000,"count":90},{"id":1571037660,"open":8306.920000000000000000,"close":8306.300000000000000000,"low":8306.200000000000000000,"high":8307.000000000000000000,"amount":5.084311000000000000,"vol":42233.572201310000000000000000000000000000,"count":57},{"id":1571037600,"open":8307.200000000000000000,"close":8306.920000000000000000,"low":8306.920000000000000000,"high":8309.160000000000000000,"amount":4.540090141728746275,"vol":37715.585646199999989163880000000000000000,"count":54}]}"""
    # ret = default_parse_restful(json_str, inner_class_name=Candlestick, default_value=None)
    # if ret and len(ret):
    #    for row in ret:
    #        row.print_object()
    #        print("========")

    pass
