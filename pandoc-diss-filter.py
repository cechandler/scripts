#!/usr/bin/env python

"""
Pandoc filter for dissertation. 
 - Filters out Code for musical notation. 
 - Adds singlespacing around Tables and BlockQuotes.
"""
from pandocfilters import toJSONFilter, RawInline, Code, Str

rhythmDict = {
	'wholeNote': '\\wholeNote{}',
	'wholeNoteDotted': '\\wholeNoteDotted{}',
	'halfNote': '\\halfNote{}',
	'halfNoteDotted': '\\halfNoteDotted{}',
	'halfNoteDown': '\\halfNoteDown{}',
	'halfNoteDottedDown': '\\halfNoteDottedDown{}',
	'halfNoteDottedDouble': '\\halfNoteDottedDouble{}',
	'quarterNote': '\\quarterNote{}',
	'halfNoteDottedDoubleDown': '\\halfNoteDottedDoubleDown{}',
	'quarterNoteDown': '\\quarterNoteDown{}',
	'quarterNoteDotted': '\\quarterNoteDotted{}',
	'quarterNoteDottedDouble': '\\quarterNoteDottedDouble{}',
	'quarterNoteDottedDown': '\\quarterNoteDottedDown{}',
	'quarterNoteDottedDoubleDown': '\\quarterNoteDottedDoubleDown{}',
	'eighthNote': '\\eighthNote{}',
	'eighthNoteDown': '\\eighthNoteDown{}',
	'eighthNoteDotted': '\\eighthNoteDotted{}',
	'eighthNoteDottedDown': '\\eighthNoteDottedDown{}',
	'eighthNoteDottedDouble': '\\eighthNoteDottedDouble{}',
	'eighthNoteDottedDoubleDown': '\\eighthNoteDottedDoubleDown{}',
	'sixteenthNote': '\\sixteenthNote{}',
	'sixteenthNoteDown': '\\sixteenthNoteDown{}',
	'sixteenthNoteDotted': '\\sixteenthNoteDotted{}',
	'sixteenthNoteDottedDown': '\\sixteenthNoteDottedDown{}',
	'sixteenthNoteDottedDouble': '\\sixteenthNoteDottedDouble{}',
	'sixteenthNoteDottedDoubleDown': '\\sixteenthNoteDottedDoubleDown{}',
	'thirtysecondNote': '\\thirtysecondNote{}',
	'thirtysecondNoteDown': '\\thirtysecondNoteDown{}',
	'thirtysecondNoteDotted': '\\thirtysecondNoteDotted{}',
	'thirtysecondNoteDottedDown': '\\thirtysecondNoteDottedDown{}',
	'thirtysecondNoteDottedDouble': '\\thirtysecondNoteDottedDouble{}',
	'thirtysecondNoteDottedDoubleDown': '\\thirtysecondNoteDottedDoubleDown{}',
}

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

def test_dynamic(x):
	if ('p' in x or 'f' in x or 'm' in x or
		'r' in x or 's' in x or 'z' in x):
		return 1
	else:
		return 0

def main(key, value, fmt, meta):
	if key == 'Code':
		[[ident, classes, keyvals], contents] = value
		if contents == '->':
			return [latex('\\textrightarrow')]
		# test if code contents is a rhythm
		if contents in rhythmDict:
			rhythm = [latex(rhythmDict[contents])]
			return rhythm
		# test code contents for slash in timesig
		elif '/' in contents and contents[0].isdigit() and len(contents) <=5:
			numerator = contents.split('/')[0]
			denominator = contents.split('/')[1]
			return [latex('\\lilyTimeSignature{' + numerator + '}{' + denominator + '}')]
		# test code contents for p, f, m, r, s, z
		elif test_dynamic(contents) == 1:
			if contents in dynamicDict:
				return [latex(dynamicDict[contents])]
			else:
				return [Str(contents)]
		# test for Ab, Bb, C#, etc...
		elif test_notename(contents[0]) == 1 and contents[1:] in accidentalDict:
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
    toJSONFilter(main)