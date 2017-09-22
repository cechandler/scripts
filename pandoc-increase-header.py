#!/usr/bin/env python

"""
Pandoc filter to
"""

from pandocfilters import toJSONFilter, Header

def header_change(key, value, format, meta):
    if key == 'Header':
        [level, [identifer, classes, kvs], text] = value
        return Header(int(level)+int(3), [identifer, classes, kvs], text)
        # if level == int(1):
        #     return Header(3, [identifer, classes, kvs], text)
        # elif level == int(2):
        #     return Header(4, [identifer, classes, kvs], text)

if __name__ == "__main__":
    toJSONFilter(header_change)
