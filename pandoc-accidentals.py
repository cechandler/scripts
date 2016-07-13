#!/usr/bin/env python

"""
Pandoc filter for producing lilyglyphs musical accidentals.
"""

from pandocfilters import toJSONFilter, RawInline, Str
import sys

# \natural
# \sharp
# \sharpArrowup
# \sharpArrowdown
# \sharpArrowboth
# \sharpSlashslashStem
# \sharpSlashslashslashStemstem
# \sharpSlashslashslashStem
# \sharpSlashslashStemstemstem
# \doublesharp
# \flatflat

def get_accidental(x):
	if x[1:] == 'bb':
		return '\\hspace*{.3ex}\\flatflat{}'
	elif x[1:] == 'b':
		return '\\hspace*{.3ex}\\flat{}'
	elif x[1:] == 'nat':
		return '\\hspace*{.3ex}\\natural{}'
	elif x[1:] == '#':
		return '\\hspace*{.3ex}\\sharp{}'
	elif x[1:] == 'x':
		return '\\hspace*{.3ex}\\doublesharp{}'
	else: 
		pass


def test_accidental(x):
	if x[1:] == 'bb':
		return 1
	elif x[1:] == 'b':
		return 1
	elif x[1:] == 'nat':
		return 1
	elif x[1:] == '#':
		return 1
	elif x[1:] == 'x':
		return 1
	else: 
		return 0


def test_notename(x):
	if (x[0] == 'A' or x[0] == 'B' or x[0] == 'C' or x[0] == 'D' or 
		x[0] == 'E' or x[0] == 'F' or x[0] == 'G'):
		return 1
	else:
		return 0
		

def latex_accidentals(key, value, format, meta):
    if (key == 'Str' and len(value) <= 4 and 
    	test_notename(value) == 1 and test_accidental(value) == 1):
		note = [Str(value[0])]
		accidental = [RawInline('latex', get_accidental(value))]
		return note + accidental

if __name__ == "__main__":
    toJSONFilter(latex_accidentals)

# TO DO:
# Rework this filter to use the same logic as pandoc-notes.py
# Where a dictionary stores all possible outputs
# And the testing is done by testing the existence of a key
# Then outputting its value if it exists