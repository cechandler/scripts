#!/usr/bin/env python

"""
Pandoc filter for wrapping Table and BlockQuote in
\singlespacing and \doublespacing
"""

from pandocfilters import toJSONFilter, RawBlock, BlockQuote, Table
import sys

# LaTeX linespacing elements
singlespacing = [RawBlock('latex', r'\singlespacing')]
doublespacing = [RawBlock('latex', r'\doublespacing')]


def addspacing(key, value, format, meta):
    if key == 'BlockQuote':
        return singlespacing + [BlockQuote(value)] + doublespacing
    elif key == 'Table':
        return singlespacing + \
            [Table(value[0], value[1], value[2], value[3], value[4])] + \
            doublespacing

if __name__ == "__main__":
    toJSONFilter(addspacing)
