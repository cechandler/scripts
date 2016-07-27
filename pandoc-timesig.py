#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs time signatures.
"""

from pandocfilters import toJSONFilter, RawInline, Span, Code, Str

def latex(x):
    return RawInline('latex', x)


def html(x):
    return RawInline('html', x)


def latex_timesig(key, value, fmt, meta):
	if key == 'Span':
		[[ident, classes, keyvals], contents] = value
		if "timesig" in classes:
			timesig = contents[0]['c']
			numerator = timesig.split('/')[0]
			denominator = timesig.split('/')[1]
			return [latex('\\lilyTimeSignature{' + numerator + '}{' + denominator + '}')]
		else:
			return None
	if key == 'Code':
		[[ident, classes, keyvals], timesig] = value
		if '/' in timesig and timesig[0].isdigit() and len(timesig) <=5:
			numerator = timesig.split('/')[0]
			denominator = timesig.split('/')[1]
			return [latex('\\lilyTimeSignature{' + numerator + '}{' + denominator + '}')]
		else:
			return None
	else:
		return None

if __name__ == "__main__":
    toJSONFilter(latex_timesig)

# TO DO
# in the Code catching portion use a try...except logic to
# test that the first and last split indices are digits
# this will allow for things like Element `A/b`

