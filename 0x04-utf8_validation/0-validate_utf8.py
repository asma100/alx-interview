#!/usr/bin/env python3
"""tasks"""


def validUTF8(data):
    """is it valid """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if n_bytes == 0:
            for i in range(8):
                if (num & (mask1 >> i)) == 0:
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:

            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
