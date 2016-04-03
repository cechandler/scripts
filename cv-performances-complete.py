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
performancesCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/performances.csv'))
worksCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/list-of-works.csv'))

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
    elif entry['Date'][0] == '2':   # skip loop if row is only a year e.g. 2014
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
    if work['End'] == 'E':
        break
    else:
        # add entries to dictionaries based on composition and year
        # workDetails.setdefault(entry['Work'],[]).append(entry)

        if work['Work'] in perfsByPiece:
            print "\subsection{%s (%s)}" % (work['Work'], work['Year'])
            print r"\b" + "egin{topic}"
            print "\setlength\itemsep{0em}"
            for perf in perfsByPiece[work['Work']]:
                if perf['Event'] == '':
                    print "\t \item[%s-%s-%s] %s -- %s, %s, %s" % (perf['Year'], perf['Month'],perf['Day'], perf['Performers'], perf['Venue'], perf['City'], perf['State'])
                else:
                    print "\t \item[%s-%s-%s] %s -- %s\\\%s, %s, %s" % (perf['Year'], perf['Month'],perf['Day'], perf['Performers'], perf['Event'], perf['Venue'], perf['City'], perf['State'])
            print "\end{topic}"
            print ""
        else:
            continue

# TO DO:
# add column(s) to performances CSV file for: selected and juried, then print those as separate headings


# ============================================================
# may be useful someday?
# html-ish output
# for work in worksCSV:
#     if work['End'] == 'E':
#         break
#     else:
#         # add entries to dictionaries based on composition and year
#         # workDetails.setdefault(entry['Work'],[]).append(entry)
#
#         print "<em>%s</em> (%s) for %s" % (work['Work'], work['Year'], work['Instrumentation'])
#         if work['Work'] in perfsByPiece:
#             for perf in perfsByPiece[work['Work']]:
#                 if perf['Event'] == '':
#                     print "\t %s-%s-%s - %s - %s, %s, %s" % (perf['Year'], perf['Month'],perf['Day'], perf['Performers'], perf['Venue'], perf['City'], perf['State'])
#                 else:
#                     print "\t %s-%s-%s - %s - %s - %s, %s, %s" % (perf['Year'], perf['Month'],perf['Day'], perf['Performers'], perf['Event'], perf['Venue'], perf['City'], perf['State'])
#         else:
#             continue
