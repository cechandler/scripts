#!/usr/bin/python
import os, time, csv, sys
from datetime import datetime
from sys import argv

# functions
def file_accessible(filepath, mode):
    ''' Check if a file exists and is accessible. '''
    try:
        print "checking %s" % (filepath)
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False
    return True

script, infile, outDir = argv

# open csv file
basepath = '/Volumes/Data/GitHub/cechandler.github.io/_data/'

if not file_accessible(basepath+infile, 'r'):
    sys.exit("\nInput file doesn't exist.\n")
else:
    perfCSV = csv.DictReader(open(basepath+infile))

for entry in perfCSV:
    # if there's a string in the Month column make the file
    if entry['Month']:
        # filename to check and be created if it doesn't exist
        perfDate = datetime.strptime(entry['Date'], '%m/%d/%y')
        postDate = perfDate.strftime("%Y-%m-%d")
        filename = postDate+'-'+entry['Composition'].replace(" ", "-")+'.md'

        # test if the filename can be opened and do this if it can
        if not file_accessible(outDir+filename, 'r'):
            target = open(outDir+filename, 'w')

            s = """
            {Month} {Day}, {Year}
            {Composition}
            """.format(
                Month = entry['Month'],
                Day = entry['Day'],
                Year = entry['Year'],
                Composition = entry['Composition']
            )
            target.write(s)
        else:
            print "%s exists." % (outDir+filename)
    else:
        continue

# TO DO:
# - get composition names with non-standard characters to print (Doppelganger) ... this might be hard
# - look up yaml front matter configuration
# - print out yaml front matter
