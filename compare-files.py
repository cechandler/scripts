#!/usr/bin/env python
import sys
from sys import argv

script, file1, file2, outfile = argv

with open(file1, 'r') as file1:
    with open(file2, 'r') as file2:
        same = set(file1).intersection(file2)
        diff = set(file2).symmetric_difference(file1)

same.discard('\n')
diff.discard('\n')

with open(outfile, 'w') as file_out:
    file_out.write('SAME\n')
    for line in same:
        file_out.write(line)
    file_out.write('\nDIFFERENCES\n')
    for line in diff:
        file_out.write(line)
