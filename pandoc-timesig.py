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
		[[ident, classes, kvs], contents] = value
		if "timesig" in classes:
			timesig = contents[0]['c']
			numerator = timesig.split('/')[0]
			denominator = timesig.split('/')[1]
			return [latex('\\lilyTimeSignature{' + numerator + '}{' + denominator + '}')]
		else:
			pass
	if key == 'Code':
		[[thing1, thing2, thing3], timesig] = value
		if '/' in timesig:
			if len(timesig) <=5:
				numerator = timesig.split('/')[0]
				denominator = timesig.split('/')[1]
				return [latex('\\lilyTimeSignature{' + numerator + '}{' + denominator + '}')]
		else:
			pass

if __name__ == "__main__":
    toJSONFilter(latex_timesig)
