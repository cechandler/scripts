#!/usr/bin/env python
import csv, sys
from sys import argv
from subprocess import call

# USAGE:
# 1) create a directory for the semester inside a syncing service (Box/Dropbox)
#    with the following structure:
#       Course Number
#           master-grades.xlsx
#           master-grades.csv
#           Students/
#               "Course Number - First Last/"
# 2) "Course Number - First Last/" is shared directly with the student via
#     Box/Dropbox/etc
# 3) master-grades.xlsx contains all students with columns for: email,
#    student ID, first name, last name, and all graded items, subtotals, final
#    grade, etc
# 4) after updating master-grades.xlsx is saved as master-grades.csv
# 5) run the script as follows:
#       python distgrades.py "Course Number" master-grades.xlsx
#  e.g. python distgrades.py "MUS 213" master-grades.xlsx

script, course, infile = argv

# basepath for course folder
# sharedpath = '/Volumes/SSD/Users/Chris/Desktop/'+course+'/' # for testing
sharedpath = '/Volumes/Data/Box Sync/2016-17-Spring/'+course+' Students/'
gradespath = '/Volumes/Data/Teaching/2016-17-Spring/'+course+'/'

# create csv from xlsx
call(["xlsx2csv", gradespath+infile, gradespath+infile+".csv"])

# open csv file
gradesCSV = csv.DictReader(open(gradespath+infile+".csv"))
for entry in gradesCSV:
    # if there's a string in the ID column make the file
    if entry['ID']:

        print "Updating %s %s grades file. " % (entry['First'], entry['Last'])

        # filename of student's first and last name
        filename = entry['First']+' '+entry['Last']+'.txt'

        # directory of the course and student first and last name
        directory = course+' - '+entry['First']+' '+entry['Last']+'/'

        with open(sharedpath+directory+filename, 'w') as target_file:

            target_file.write('%s \nSpring 2017 \n%s %s\n\n' % (course, entry['First'], entry['Last']))

            if entry['A1'] or entry['A1C']:
                target_file.write('ASSIGNMENTS \nAssign 1: %s \n' % entry['A1'])
                target_file.write('Comments: %s \n\n' % entry['A1C'])

            if entry['A2'] or entry['A2C']:
                target_file.write('Assign 2: %s \n' % entry['A2'])
                target_file.write('Comments: %s \n\n' % entry['A2C'])

            if entry['A3'] or entry['A3C']:
                target_file.write('Assign 3: %s \n' % entry['A3'])
                target_file.write('Comments: %s \n\n' % entry['A3C'])

            if entry['A4'] or entry['A4C']:
                target_file.write('Assign 4: %s \n' % entry['A4'])
                target_file.write('Comments: %s \n\n' % entry['A4C'])

            if entry['A5'] or entry['A5C']:
                target_file.write('Assign 5: %s \n' % entry['A5'])
                target_file.write('Comments: %s \n\n' % entry['A5C'])

            if entry['A6'] or entry['A6C']:
                target_file.write('Assign 6: %s \n' % entry['A6'])
                target_file.write('Comments: %s \n\n' % entry['A6C'])

            if entry['A7'] or entry['A7C']:
                target_file.write('Assign 7: %s \n' % entry['A7'])
                target_file.write('Comments: %s \n\n' % entry['A7C'])

            if entry['A8'] or entry['A8C']:
                target_file.write('Assign 8: %s \n' % entry['A8'])
                target_file.write('Comments: %s \n\n' % entry['A8C'])

            if entry['A9'] or entry['A9C']:
                target_file.write('Assign 9: %s \n' % entry['A9'])
                target_file.write('Comments: %s \n\n' % entry['A9C'])

            if entry['A10'] or entry['A10C']:
                target_file.write('Assign 10: %s \n' % entry['A10'])
                target_file.write('Comments: %s \n\n' % entry['A10C'])

            if entry['A11'] or entry['A11C']:
                target_file.write('Assign 11: %s \n' % entry['A11'])
                target_file.write('Comments: %s \n\n' % entry['A11C'])

            if entry['A12'] or entry['A12C']:
                target_file.write('Assign 12: %s \n' % entry['A12'])
                target_file.write('Comments: %s \n\n' % entry['A12C'])

            if entry['Q1 sub']:
                target_file.write('QUIZZES \nQ1: %s\n' % entry['Q1 sub'])

            if entry['Q2 sub']:
                target_file.write('Q2: %s\n' % entry['Q2 sub'])

            if entry['Q3 sub']:
                target_file.write('Q3: %s\n' % entry['Q3 sub'])

            if entry['Q4 sub']:
                target_file.write('Q4: %s\n' % entry['Q4 sub'])

            if entry['Q5 sub']:
                target_file.write('Q5: %s\n' % entry['Q5 sub'])

            if entry['Proj 1']:
                target_file.write('\nPROJECTS \nProject 1: %s\n' % entry['Proj 1'])

            if entry['Proj 2']:
                target_file.write('Project 2: %s\n' % entry['Proj 2'])

            if entry['Proj 3']:
                target_file.write('Project 3: %s\n' % entry['Proj 3'])

            if entry['Proj 4']:
                target_file.write('Project 4: %s\n' % entry['Proj 4'])

            if entry['Proj 5']:
                target_file.write('Project 5: %s\n' % entry['Proj 5'])

            if entry['Exam 1']:
                target_file.write('\nEXAMS \nExam 1: %s\n' % entry['Exam 1'])

            if entry['Exam 2']:
                target_file.write('Exam 2: %s\n' % entry['Exam 2'])

            if entry['Attend']:
                target_file.write('\nAttendance: %s\n' % entry['Attend'])

            if entry['Part']:
                target_file.write('Participation: %s\n' % entry['Part'])

        print "Finished updating %s %s grades file. " % (entry['First'], entry['Last'])

    else:
        continue
