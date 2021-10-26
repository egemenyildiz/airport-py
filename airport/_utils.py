import logging
import subprocess
import re
import _datatypes as datatypes
import os

from airport._constants import SCAN_RESULTS_GROUPED_PATTERN

AIRPORT_PATH = [os.environ.get(
    'AIRPORT_PATH', 
    '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')]


def call_cmd(*args):
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    process.wait()
    return out


def split_lines(lines, start=0, remove_empty_lines=True):
    split = lines.split('\n')[start:]
    if remove_empty_lines:
        return filter(None, split)
    return split


def reformat_scan_results(results):
    def clean_line(result):
        matches = re.match(re.compile(SCAN_RESULTS_GROUPED_PATTERN, re.IGNORECASE), result)
        if matches:
            cleaned_node = {k: v.strip() for k, v in matches.groupdict().items()}
            return datatypes.NodeResult(**cleaned_node)
        logging.error('Parse error: {}'.format(result))

    lines = split_lines(results, start=1)
    cleaned = filter(None, map(clean_line, lines))
    return cleaned


def reformat_info_result(result):
    def reformat_info_result_line(line):
        _, value = line.split(':', 1)
        return value.strip()

    results_in_lines = filter(lambda line: line, split_lines(result))
    info_args = map(reformat_info_result_line, results_in_lines)
    return datatypes.InfoResult(*info_args)


def build_airport_cmd(params):
    return AIRPORT_PATH + params
