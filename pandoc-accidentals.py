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
		# test for Ab, Bb, C#, etc...
		if test_notename(contents[0]) == 1 and contents[1:] in accidentalDict:
			note = [Str(contents[0])]
			accidental = [RawInline('latex', accidentalDict[contents[1:]])]
			return note + accidental
		# test for Ab4, Bb2, C#6, etc...
		elif test_notename(contents[0]) == 1 and contents[-1].isdigit() and contents[1:-1] in accidentalDict:
			note = [Str(contents[0])]
			registerNum = [Str(contents[-1])]
			accidental = [RawInline('latex', accidentalDict[contents[1:-1]])]
			return note + accidental + registerNum
		# test for A4, B5, C6, etc...
		elif test_notename(contents[0]) == 1 and contents[-1].isdigit() and len(contents) == 2:
			note = [Str(contents[0])]
			registerNum = [Str(contents[-1])]
			return note + registerNum
		# test for A, B, C, etc...
		elif test_notename(contents[0]) == 1 and len(contents) == 1:
			note = [Str(contents[0])]
			return note
		else:
			return None
	else:
		return None

if __name__ == "__main__":
    toJSONFilter(latex_accidentals)

# TO DO
