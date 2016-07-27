#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs musical rhythms.
"""

from pandocfilters import toJSONFilter, RawInline, Code, Str

dynamicDict = {
	'pppp': '\\lilyDynamics{pppp}',
	'ppp': '\\lilyDynamics{ppp}',
	'pp': '\\lilyDynamics{pp}',
	'p': '\\lilyDynamics{p}',
	'mp': '\\lilyDynamics{mp}',
	'mf': '\\lilyDynamics{mf}',
	'f': '\\lilyDynamics{f}',
	'ff': '\\lilyDynamics{ff}',
	'fff': '\\lilyDynamics{fff}',
	'ffff': '\\lilyDynamics{ffff}',
	'sf': '\\lilyDynamics{sf}',
	'sff': '\\lilyDynamics{sff}',
	'sfff': '\\lilyDynamics{sfff}',
	'sffff': '\\lilyDynamics{sffff}',
	'sfz': '\\lilyDynamics{sfz}',
	'sffz': '\\lilyDynamics{sffz}',
	'sfffz': '\\lilyDynamics{sfffz}',
	'sffffz': '\\lilyDynamics{sffffz}',
}

def latex(x):
    return RawInline('latex', x)

def html(x):
    return RawInline('html', x)

def test_dynamic(x):
	if ('p' in x or 'f' in x or 'm' in x or
		'r' in x or 's' in x or 'z' in x):
		return 1
	else:
		return 0

def latex_dynamics(key, value, fmt, meta):
	if key == 'Code':
		[[ident, classes, keyvals], contents] = value
		if test_dynamic(contents) == 1:
			if contents in dynamicDict:
				return [latex(dynamicDict[contents])]
			else:
				return [Str(contents)]
		else:
			return None
	else:
			return None

if __name__ == "__main__":
    toJSONFilter(latex_dynamics)
