#Parce CSV

import csv		#imports libraries used to read the csv files
#import codecs 	#import codecs library to decode csv
#import string

def parsCsv(csvLocation):
	#docLinks is a multi dimensional list to compensate for multiple documents with each project 
	#the list is structured like the comment below
	#[project0Title, doc0A, doc0B, doc0C, doc0D, doc0E],[project1Title, doc1A, doc1B, doc1C, doc1D, doc1E] 
	docLinks = []
	
	with open(csvLocation, 'rU') as csvfile:			#open the CSV file
		reader = csv.reader(csvfile, delimiter = ',')	#set the seperation charicter
		for row in reader:								#read untill there are no rows left
			if(row[3].lower() != "email"):				#exclude the title Email from the list
				docLinks.append(row[3])					#append the documentation links to the multidimensional list
	return docLinks

'''*************************************************************'''
'''************************** Test Call ************************'''
'''*** uncomment the lines below to run this def by its self ***'''
'''*************************************************************'''

'''
docLinks = []
docLinks = parsCsv('testFile1.csv')
counter = 0

for lines in docLinks:
	print counter, lines
	counter = counter + 1
'''