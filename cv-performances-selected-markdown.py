#!/usr/bin/python
import csv, sys, os, pprint
from datetime import datetime
from collections import defaultdict

# remove unnecessary columns from csvfile
def removekeys(d, k):
    for item in k:
    	del d[item]
    return d

# open csv files
# performancesCSV = csv.DictReader(open(str(sys.argv[1])))
# performancesCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/performances.csv'))
# worksCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/list-of-works.csv'))

def fitem(item):
    item=item.strip()
    try:
        item=float(item)
    except ValueError:
        pass
    return item

with open('/Users/cc7zv/GitHub/cechandler.github.io/_data/performances.csv', 'rU') as csvin:
    reader = csv.DictReader(csvin)
    data = {k.strip():[fitem(v)] for k,v in reader.next().items()}
    for line in reader:
        for k,v in line.items():
            k=k.strip()
            data[k].append(fitem(v))

# pprint.pprint(data)

count = 0
while count < len(data['Special']):
    if 'S' in data['Special'][count]:
        perfDate = datetime.strptime(data['Date'][count], '%m/%d/%y')
        print "%s/%s/%s" % (perfDate.strftime('%Y'), perfDate.strftime('%m'), perfDate.strftime('%d'))
        print ": *%s* - %s - %s, %s \n" % (data['Composition'][count], data['Performers'][count], data['City'][count], data['State'][count])
        count += 1
    else:
        count += 1
