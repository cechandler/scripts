#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs musical accidentals.
"""

from pandocfilters import toJSONFilter, RawInline, Str, Div, Plain

def latex(x):
    return RawInline('latex', x)


def html(x):
    return RawInline('html', x)


def latex_timesig(key, value, fmt, meta):
	if key == 'Div':
		[[ident, classes, kvs], contents] = value
		if "timesig" in classes:
			for item in contents:
				[kind, sig] = item
				block = sig[0][0]

				# if key == 'Plain':
				# 	return Str('BOO!')
			# 	[key, sig] = item
			# 	if key == 'Plain':
			# 		numerator = sig.split('/')[0]
			# 		denominator = sig.split('/')[1]
			# 		return(
			# 			[latex('\\lilyTimeSignature{' + numerator +
			# 			'}{' + denominator + '}')])

if __name__ == "__main__":
    toJSONFilter(latex_timesig)
