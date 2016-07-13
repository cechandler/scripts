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
	if x == 'bb':
		return '\\hspace*{.3ex}\\flatflat{}'
	elif x == 'b':
		return '\\hspace*{.3ex}\\flat{}'
	elif x == 'nat':
		return '\\hspace*{.3ex}\\natural{}'
	elif x == '#':
		return '\\hspace*{.3ex}\\sharp{}'
	elif x == 'x':
		return '\\hspace*{.3ex}\\doublesharp{}'
	else: 
		pass


def test_accidental(x):
	if ('bb' in x or 'b' in x or 'nat' in x or
		'#' in x or 'x' in x):
		return 1
	# if x[1:] == 'bb':
	# 	return 1
	# elif x[1:] == 'b':
	# 	return 1
	# elif x[1:] == 'nat':
	# 	return 1
	# elif x[1:] == '#':
	# 	return 1
	# elif x[1:] == 'x':
	# 	return 1
	else: 
		return 0


def test_notename(x):
	if ('A' in x or 'B' in x or 'C' in x or 'D' in x or
		'E' in x or 'F' in x or 'G' in x):
		return 1
	# if (x[0] == 'A' or x[0] == 'B' or x[0] == 'C' or x[0] == 'D' or 
	# 	x[0] == 'E' or x[0] == 'F' or x[0] == 'G'):
	# 	return 1
	# if (x == 'A' or x == 'B' or x == 'C' or x == 'D' or 
	# 	x == 'E' or x == 'F' or x == 'G'):
	# 	return 1
	else:
		return 0
		

def latex_accidentals(key, value, format, meta):
    if (key == 'Str' and len(value) <= 4 and 
        test_accidental(value) == 1 and test_notename(value) == 1):
    	if value[0] == '(':
			note = [Str(value[1])]
			accidental = [RawInline('latex', get_accidental(value[2:]))]
			return note + accidental
		else:
			note = [Str(value[0])]
			accidental = [RawInline('latex', get_accidental(value[1:]))]
			return note + accidental
  #   if (key == 'Str' and len(value) <= 4 and 
  #   	test_notename(value) == 1 and test_accidental(value) == 1):
		# note = [Str(value[0])]
		# accidental = [RawInline('latex', get_accidental(value))]
		# return note + accidental

if __name__ == "__main__":
    toJSONFilter(latex_accidentals)
