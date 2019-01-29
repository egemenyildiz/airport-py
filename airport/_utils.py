import subprocess
import re
import _datatypes as datatypes
import os 

AIRPORT_PATH = [os.environ.get(
    'AIRPORT_PATH', 
    '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')]


def call_cmd(*args):
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    process.wait()
    return out


def split_lines(lines, start=0):
    return lines.split('\n')[start:]


def reformat_scan_results(results):
    def reformat_scan_result_line(result):
        try:
            result = re.split('\s+', result)
            node_args = (result[1:5] + [True if result[5] == 'Y' else False, ] +
                         [result[6] if result[6] != '--' else None] +
                         [' '.join(result[7:]).strip()])
        except IndexError:
            pass
        else:
            return datatypes.NodeResult(*node_args)

    results_in_lines = split_lines(results, start=1)
    return filter(None, map(reformat_scan_result_line, results_in_lines))


def reformat_info_result(result):
    def reformat_info_result_line(line):
        _, value = line.split(':', 1)
        return value.strip()

    results_in_lines = filter(lambda line: line, split_lines(result))
    info_args = map(reformat_info_result_line, results_in_lines)
    return datatypes.InfoResult(*info_args)

def build_airport_cmd(params):
    return AIRPORT_PATH + params
