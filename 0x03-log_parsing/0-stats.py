#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """

import sys
import re


def print_log(log_to_print : dict) -> None:
    """ print_log function """
    print("File size: {}".format(log_to_print["size"]))
    for status_code in log_to_print["code_count"]:
        if log_to_print["code_count"][status_code] != 0:
            print("{}: {}".format(status_code, log_to_print["code_count"][status_code]))


if __name__ == "__main__":
    REGEX = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \
            d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    compiled = re.compile(REGEX)

    lines = 0
    log = {}
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 
            0, 404: 0, 405: 0, 500: 0}
    log["code_count"] = dict.fromkeys(status_codes, 0)
    log["size"] = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            full_match = compiled.fullmatch(line)
            if (full_match is not None):
                code = full_match.group(1)
                size = int(full_match.group(2))

                if (code.isnumeric()):
                    log["code_count"][int(code)] = log["code_count"][int(code)] + 1

                log["size"] = log["size"] + size
                lines = lines + 1
                if (lines % 10 == 0):
                    print_log(log)
    finally:
        print_log(log)
