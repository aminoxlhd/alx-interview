#!/usr/bin/python3
""" determines if a given data set represents a valid UTF-8 encoding """


def validUTF8(data):
    """ validUTF8 function """
    bytes_count = 0
    for d in data:
        if 191 >= d and d >= 128:
            if not bytes_count:
                return False

            bytes_count = bytes_count - 1
        else:
            if bytes_count:
                return False

            if d < 128:
                continue
            if d < 224:
                bytes_count = 1
            elif d < 240:
                bytes_count = 2
            elif d < 248:
                bytes_count = 3
            else:
                return False

    return bytes_count == 0
