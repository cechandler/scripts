#!/usr/bin/env python
import csv, sys
from sys import argv
from subprocess import call

# USAGE:
# 1) create a directory for the semester inside a syncing service (Box/Dropbox)
#    with the following structure:
#       Course Num
#           master-grades.xlsx
#           master-grades.csv
#           Students/
#               "Course Num - First Last/"
# 2) "Course Num - First Last/" is shared directly with the student via
#     Box/Dropbox/etc
# 3) master-grades.xlsx contains all students with columns for: email,
#    student ID, first name, last name, and all graded items, subtotals, final
#    grade, etc
# 4) after updating master-grades.xlsx is saved as master-grades.csv
# 5) run the script as follows:
#       python distgrades.py "Course Num" master-grades.xlsx
#  e.g. python distgrades.py "MUS 213" master-grades.xlsx

script, course, infile = argv

# basepath for course folder
sharedpath = '/Volumes/Data/Box Sync/2016-17-Fall/'+course+'/'
gradespath = '/Volumes/Data/Teaching/2016-17-Fall/'+course+'/'

# create csv from xlsx
call(["xlsx2csv", gradespath+infile, gradespath+infile+".csv"])

# open csv file
gradesCSV = csv.DictReader(open(gradespath+infile+".csv"))
for entry in gradesCSV:
    # if there's a string in the ID column make the file
    if entry['ID']:
        # filename of student's first and last name
        filename = entry['First']+' '+entry['Last']+'.txt'
        # directory of the course and student first and last name
        directory = course+' - '+entry['First']+' '+entry['Last']+'/'
        target = open(sharedpath+directory+filename, 'w')

        s = """
        {Course}
        Fall 2016
        {First} {Last}

        ASSIGNMENTS
        Assign 1: {A1}
        Comments: {A1C}

        Assign 2: {A2}
        Comments: {A2C}

        Assign 3: {A3}
        Comments: {A3C}

        Assign 4: {A4}
        Comments: {A4C}

        Assign 5: {A5}
        Comments: {A5C}

        Assign 6: {A6}
        Comments: {A6C}

        Assign 7: {A7}
        Comments: {A7C}

        Assign 8: {A8}
        Comments: {A8C}

        Assign 9: {A9}
        Comments: {A9C}

        Assign 10: {A10}
        Comments: {A10C}

        Assign 11: {A11}
        Comments: {A11C}

        Assign 12: {A12}
        Comments: {A12C}

        Assign 13: {A13}
        Comments: {A13C}

        QUIZZES
        Q1: {Q1}
        Q2: {Q2}
        Q3: {Q3}
        Q4: {Q4}
        Q5: {Q5}

        PROJECTS
        Project 1: {P1}
        Project 2: {P2}
        Project 3: {P3}

        EXAMS
        Exam 1: {E1}
        Exam 2: {E2}

        Attendance:
        Participation:

        """.format(
            Course = course,
            First = entry['First'],
            Last = entry['Last'],
            A1 = entry['A1'],
            A2 = entry['A2'],
            A3 = entry['A3'],
            A4 = entry['A4'],
            A5 = entry['A5'],
            A6 = entry['A6'],
            A7 = entry['A7'],
            A8 = entry['A8'],
            A9 = entry['A9'],
            A10 = entry['A10'],
            A11 = entry['A11'],
            A12 = entry['A12'],
            A13 = entry['A13'],
            A1C = entry['A1C'],
            A2C = entry['A2C'],
            A3C = entry['A3C'],
            A4C = entry['A4C'],
            A5C = entry['A5C'],
            A6C = entry['A6C'],
            A7C = entry['A7C'],
            A8C = entry['A8C'],
            A9C = entry['A9C'],
            A10C = entry['A10C'],
            A11C = entry['A11C'],
            A12C = entry['A12C'],
            A13C = entry['A13C'],
            P1 = entry['Proj 1'],
            P2 = entry['Proj 2'],
            P3 = entry['Proj 3'],
            Q1 = entry['Q1'],
            Q2 = entry['Q2'],
            Q3 = entry['Q3'],
            Q4 = entry['Q4'],
            Q5 = entry['Q5'],
            E1 = entry['Exam 1'],
            E2 = entry['Exam 2']
        )
        target.write(s)
    else:
        continue
