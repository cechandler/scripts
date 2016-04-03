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
# performancesCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/performances.csv'))
# worksCSV = csv.DictReader(open('/Volumes/Data/Dropbox/Website/list-of-works.csv'))

def fitem(item):
    item=item.strip()
    try:
        item=float(item)
    except ValueError:
        pass
    return item

with open('/Volumes/Data/Dropbox/Website/performances.csv', 'r') as csvin:
    reader = csv.DictReader(csvin)
    data = {k.strip():[fitem(v)] for k,v in reader.next().items()}
    for line in reader:
        for k,v in line.items():
            k=k.strip()
            data[k].append(fitem(v))

count = 0
print "\section{Selected Performances}"
print r"\b" + "egin{topic}"
print "\setlength\itemsep{0em}"
while count < len(data['Sel']):
    if 'S' in data['Sel'][count]:
        perfDate = datetime.strptime(data['Date'][count], '%m/%d/%y')
        print "\t \item[%s/%s/%s] \emph{%s} -- %s -- %s, %s" % (perfDate.strftime('%Y'), perfDate.strftime('%m'), perfDate.strftime('%d'), data['Composition'][count], data['Performers'][count], data['City'][count], data['State'][count])
        count += 1
    else:
        count += 1
print "\end{topic}"
