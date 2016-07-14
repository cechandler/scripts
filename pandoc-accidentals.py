#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs musical accidentals.
"""

from pandocfilters import toJSONFilter, RawInline, Code, Str

accidentalDict = {
	'nat': '\\hspace*{.3ex}\\natural{}',
	'b': '\\hspace*{.3ex}\\flat{}',
	'#': '\\hspace*{.3ex}\\sharp{}',
	'x': '\\hspace*{.3ex}\\doublesharp{}',
	'bb': '\\hspace*{.3ex}\\flatflat{}',
	'sharpArrowup': '\\hspace*{.3ex}\\sharpArrowup{}',
	'sharpArrowdown': '\\hspace*{.3ex}\\sharpArrowdown{}',
	'sharpArrowboth': '\\hspace*{.3ex}\\sharpArrowboth{}',
	'sharpSlashslashStem': '\\hspace*{.3ex}\\sharpSlashslashStem{}',
	'sharpSlashslashslashStemstem': '\\hspace*{.3ex}\\sharpSlashslashslashStemstem{}',
	'sharpSlashslashslashStem': '\\hspace*{.3ex}\\sharpSlashslashslashStem{}',
	'sharpSlashslashStemstemstem': '\\hspace*{.3ex}\\sharpSlashslashStemstemstem{}',
}

def latex(x):
    return RawInline('latex', x)


def html(x):
    return RawInline('html', x)


def test_notename(x):
	if (x == 'A' or x == 'B' or x == 'C' or x == 'D' or 
		x == 'E' or x == 'F' or x == 'G'):
		return 1
	else:
		return 0


def latex_accidentals(key, value, fmt, meta):
	if key == 'Code':
		[[thing1, thing2, thing3], contents] = value
		if test_notename(contents[0]) == 1 and contents[1:] in accidentalDict:
			note = [Str(contents[0])]
			accidental = [RawInline('latex', accidentalDict[contents[1:]])]
			return note + accidental
		else:
			return None
	else:
		return None

if __name__ == "__main__":
    toJSONFilter(latex_accidentals)

# TO DO
# - test notname and then test contents[1:] for nothing
# - if nothing, then single note and return Str(contents[0])