import csv
import math
import sets
import numpy

def interpret_string(s):
    if not isinstance(s, str):
        return str(s)
    if s.isdigit():
        return int(s)
    try:
        return float(s)
    except:
        return s
        
def repr_with_spaces(lst):
    return repr(lst).replace(",", " ")
 
data = [row for row in csv.reader(open('/Users/Chris/Dropbox/2012-13Spring/Beethoven/FinalPaper/SQ15_MIDImap/MIDI/StringQuartet15_Mvmt1NoTempoNoTiesRAW.csv', "rU"))]

list_of_bars = []
list_of_attacks = []
for n in range(265):
	list_of_bars.append( [] )
	list_of_attacks.append ( [] )

rowcount = 1
while rowcount < len(data):
	if data[rowcount][2] == " Note_on_c":
		pitch = int(data[rowcount][4])-60
		attacks = int(data[rowcount][1])
		bar = 1+int(math.floor(interpret_string(data[rowcount][1])/3840))
		list_of_bars[bar].append(pitch)
		list_of_attacks[bar].append(attacks)
		rowcount += 1
	else:
		pass
		rowcount +=1

for n in range(1, 265):
	pitches = list(sets.Set(list_of_bars[n]))
	pitches.sort()
	sortedPitches = repr_with_spaces(pitches)
	highPitch = max(pitches)
	lowPitch = min(pitches)
	meanPitch = round(numpy.mean(pitches), 3)
	numPitches = len(pitches)
	numAttacks = len(list(sets.Set(list_of_attacks[n])))
	if numPitches == 1:
		bandwidth == 0
	else:
		bandwidth = highPitch + abs(lowPitch)
	print "%s, %s, %s, %s, %s, %s, %s, %s" % (n, highPitch, sortedPitches, lowPitch, meanPitch, numPitches, bandwidth, numAttacks)

# 	print "Bar %s" % (n)
# 	print "Top Pitch: %s" % (highPitch)
# 	print "Total Pitches: %s" % (pitches)
# 	print "Low Pitch: %s" % (lowPitch)
# 	print "Mean Pitch: %s" % (meanPitch)
# 	print "Num Diff Pitches: %s" % (numPitches)
# 	print "Bandwidth: %s" % (bandwidth)
# 	print "Num Attacks: %s" % (numAttacks)
# 	print ""
#     
# # for n in range(264):
# #     list_name = 'bar_'+str(n)
# #     exec(list_name + ' = []')
# #     exec('print ' + list_name)