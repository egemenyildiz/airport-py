# -*- coding: utf-8 -*-
import _utils


def scan():
    cmd = _utils.build_airport_cmd(params=['-s'])
    results = _utils.call_cmd(*cmd)
    return _utils.reformat_scan_results(results)


def info():
    cmd = _utils.build_airport_cmd(params=['-I'])
    result = _utils.call_cmd(*cmd)
    return _utils.reformat_info_result(result)
