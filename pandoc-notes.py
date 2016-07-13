#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs musical notes.
"""

from pandocfilters import toJSONFilter, RawInline, Code, Str

notes = {
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

def latex(x):
    return RawInline('latex', x)


def html(x):
    return RawInline('html', x)


def latex_notes(key, value, fmt, meta):
	if key == 'Code':
		[[thing1, thing2, thing3], timesig] = value
		if timesig in notes:
			return [latex(notes[timesig])]
		else:
			return None

if __name__ == "__main__":
    toJSONFilter(latex_notes)
