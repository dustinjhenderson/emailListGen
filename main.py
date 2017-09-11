#main script
#This script pulls all the pieces together
#Call each part here when they are all completed

import csv		#imports libraries used to read the csv files
#import string

from append import append
from parsCsv import parsCsv

#listFromCsv = []
csvLocation = "testFile1.csv"

print "CSV open"

listFromCsv = parsCsv(csvLocation) 

for line in listFromCsv:
	print line

print "File Open"
	
append(listFromCsv)