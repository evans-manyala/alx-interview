#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Number of bytes in the current UTF-8 character
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
