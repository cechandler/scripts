#!/usr/bin/python
import csv, sys
from datetime import datetime
from collections import defaultdict

# remove unnecessary columns from csvfile
def removekeys(d, k):
    for item in k:
    	del d[item]
    return d

# open csv files
# performancesCSV = csv.DictReader(open(str(sys.argv[1])))
performancesCSV = csv.DictReader(open('/Volumes/Data/GitHub/cechandler.github.io/_data/performances.csv'))
worksCSV = csv.DictReader(open('/Volumes/Data/GitHub/cechandler.github.io/_data/works.csv'))

# create empty dictionaries
perfsByPiece = {}
perfsByYear = {}
workDetails = {}

# collect all performances in perfsByPiece and perfsByYear
for entry in performancesCSV:
    if entry['R'] == 'E':           # stop loop if end of file
        break
    elif entry['R'] == 'X':         # skip loop if entry should not be included
        continue
    elif entry['Composition'] == '':   # skip loop if row is only a year e.g. 2014
        continue
    else:
        entry = removekeys(entry, ['R']) # remove unnecessary keys from entries (is this necessary?)

        # add separate key/values for Year, Month, and Day from Date
        # entry['Month'] = perfDate.strftime('%b') # abbreviated month, e.g. Jan
        perfDate = datetime.strptime(entry['Date'], '%m/%d/%y')
        entry['Year'] = perfDate.strftime('%Y')
        entry['Month'] = perfDate.strftime('%m')
        entry['Day'] = perfDate.strftime('%d')

        # add entries to dictionaries based on composition and year
        perfsByPiece.setdefault(entry['Composition'],[]).append(entry)
        perfsByYear.setdefault(entry['Year'],[]).append(entry)

for work in worksCSV:
    if work['Special'] == 'E':
        break
    else:
        # add entries to dictionaries based on composition and year
        # workDetails.setdefault(entry['Work'],[]).append(entry)

        if work['Work'] in perfsByPiece:
            print "## %s (%s)" % (work['Work'], work['Year'])
            for perf in perfsByPiece[work['Work']]:
                if perf['Event'] == '':
                    print "%s-%s-%s" % (perf['Year'], perf['Month'],perf['Day'])
                    print ": %s - %s, %s, %s" % (perf['Performers'], perf['Venue'], perf['City'], perf['State'])
                    print ""
                else:
                    print "%s-%s-%s" % (perf['Year'], perf['Month'],perf['Day'])
                    print ": %s - %s\n: %s, %s, %s" % (perf['Performers'], perf['Event'], perf['Venue'], perf['City'], perf['State'])
                    print ""
        else:
            continue

# TO DO:

# write output to a file that can the be read into CV and web pages
# add column(s) to performances CSV file for: selected and juried, then print those as separate headings
