#!/usr/bin/env python

"""
Pandoc filter to convert instances of Switch~ to
Switch\\mytilde which produces a better tilde.
"""

from pandocfilters import toJSONFilter, Str, RawInline

def latex(x):
    return RawInline('latex', x)

def switch(key, value, format, meta):
    if key == 'Str' and value == 'Switch~':
        return [latex('Switch\\mytilde')]

if __name__ == "__main__":
    toJSONFilter(switch)
