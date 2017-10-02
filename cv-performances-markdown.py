#!/usr/bin/python
import argparse
import csv
import os
import sys
import pprint
from datetime import datetime
from collections import defaultdict

# ARGUMENTS
parser = argparse.ArgumentParser(
    description="a script that reads performance and composition csv files and\
    outputs a list of performances in markdown")
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--complete', action='store_true',
                   default=False, help='outputs complete list of performances')
group.add_argument('-e', '--ensemble', action='store_true',
                   default=False, help='outputs notable ensemble performances')
group.add_argument('-j', '--juried', action='store_true',
                   default=False, help='outputs juried festival performances')
group.add_argument('-s', '--selected', action='store_true',
                   default=False, help='outputs selected performances')

parser.add_argument('-i', '--input', action='store',
                    default=os.path.join(os.environ['CECSITE'], '_data/'),
                    help='input directory for performances.csv and works.csv')
parser.add_argument('-o', '--output', action='store', default='./',
                    help='output directory for resulting markdown file')

args = parser.parse_args()

# DICTIONARIES
perfsByPiece = {}
perfsByYear = {}
workDetails = {}

# FILES
performancesPath = str(args.input) + "performances.csv"
worksPath = str(args.input) + "works.csv"

# open the csv files
performancesCSV = csv.DictReader(open(performancesPath, 'rU'))
worksCSV = csv.DictReader(open(worksPath, 'rU'))

# collect all performances in perfsByPiece and perfsByYear
for row in performancesCSV:
    if row['Composition'] == '':
        # skip row if composition listing is missing (e.g. year heading)
        continue
    else:
        # add entries to dictionaries based on composition and year
        perfsByPiece.setdefault(row['Composition'],[]).append(row)
        perfsByYear.setdefault(row['Year'],[]).append(row)

# pprint.pprint(perfsByPiece) # for testing

if args.complete:

    for work in worksCSV:
        if work['Title'] in perfsByPiece:
            print "## %s (%s)\n" % (work['Title'], work['Year'])
            for perf in perfsByPiece[work['Title']]:
                if perf['Event'] == '':
                    print "%s-%s-%s" % (perf['Year'], perf['Month'].zfill(2),perf['Day'].zfill(2))
                    print ": %s - %s, %s, %s\n" % (perf['Performers'], perf['Venue'], perf['City'], perf['State'])
                else:
                    print "%s-%s-%s" % (perf['Year'], perf['Month'].zfill(2),perf['Day'].zfill(2))
                    print ": %s - %s\n: %s, %s, %s\n" % (perf['Performers'], perf['Event'], perf['Venue'], perf['City'], perf['State'])
        else:
            continue

elif args.ensemble:

    print("\nFunctionality coming soon.")

elif args.juried:

    # get the current year
    year = str(datetime.now().year)
    # for every year from 2008 until current year (+1 needed bc range outputs -1)
    for year in reversed(range(2008, int(year)+1)):
        printCurrentYear = True
        if str(year) in perfsByYear:
            for perf in perfsByYear[str(year)]:
                if 'J' in perf['Special']:
                    if printCurrentYear == True:
                        if str(year) == str(datetime.now().year):
                            print "%s" % (year)
                        else:
                            print "\n%s" % (year)
                        printCurrentYear = False
                    print ": %s, %s, %s" % (perf['Event'], perf['City'], perf['State'])
                else:
                    continue

elif args.selected:

    # reopen performancesCSV after opening and filling dictionaries in line 46
    performancesCSV = csv.DictReader(open(performancesPath, 'rU'))
    for row in performancesCSV:
        if 'S' in row['Special']:
            perfDate = datetime.strptime(row['Date'], '%m/%d/%y')
            print "%s-%s-%s" % (perfDate.strftime('%Y'), perfDate.strftime('%m'), perfDate.strftime('%d'))
            print ": *%s* - %s, %s, %s \n" % (row['Composition'], row['Performers'], row['City'], row['State'])
        else:
            continue

else:

    print("\nNeeds arguments. Please run script with --help.\n")


# # TO DO:
#
# Write a function for the similar code in selected and juried
#     - pass in flag to find (e.g., S or J or ...) which is used in if statement
#     -
