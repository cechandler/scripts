#!/usr/bin/env python

"""
Pandoc filter for wrapping Table and BlockQuote in
\singlespacing and \doublespacing
"""

from pandocfilters import toJSONFilter, RawBlock, BlockQuote, Table
import sys
import signal

# LaTeX linespacing elements
singlespacing = [RawBlock('latex', r'\singlespacing')]
doublespacing = [RawBlock('latex', r'\doublespacing')]

def latex(x):
	return RawBlock('latex', x)

def addspacing(key, value, format, meta):
    if key == 'BlockQuote':
        # return [latex('\\singlespacing')] + [BlockQuote(value)] + [latex('\\doublespacing')]
        return singlespacing + [BlockQuote(value)] + doublespacing
    elif key == 'Table':
        return singlespacing + \
            [Table(value[0], value[1], value[2], value[3], value[4])] + \
            doublespacing

if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL) 
    toJSONFilter(addspacing)
    # sys.stdout.flush()
