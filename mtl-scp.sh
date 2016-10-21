#!/bin/bash

# to get IP address: ipconfig getifaddr en0

lab[1]="141.166.220.210"
lab[2]="141.166.222.136"
lab[3]="141.166.222.65"
lab[4]="141.166.222.113"
lab[5]="141.166.222.203"
lab[6]="141.166.220.91"
lab[7]="141.166.220.246"
lab[8]="141.166.221.125"
lab[9]="141.166.220.79"
lab[10]="141.166.222.183"
lab[11]="141.166.221.89"
lab[12]="141.166.220.217"
lab[13]="141.166.221.46"
lab[14]="141.166.220.28"
lab[15]="141.166.222.182"

for i in $lab;
do
	scp -r "/Volumes/Data/Teaching/2016-17-Fall/MUS 338/exams/Exam 1/exam1-part1-mix-analysis.mp3" musiclabuser@$i:~/Desktop
done
