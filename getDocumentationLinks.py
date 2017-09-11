#Get Documentation Links from the anaylitics csv file
#downloaded from the design store. This file uses the
#file in its csv format. This module requiers the name
#and location of the csv file to run.
#Dustin Henderson

import csv	#imports libraries used to read the csv files

def getDocLinks(csvLocation):
	#docLinks is a multi dimensional list to compensate for multiple documents with each project 
	#the list is structured like the comment below
	#[project0Title, doc0A, doc0B, doc0C, doc0D, doc0E],[project1Title, doc1A, doc1B, doc1C, doc1D, doc1E] 
	docLinks = []
	with open(csvLocation, 'rb') as table:			#open the CSV file
		reader = csv.reader(table, delimiter=',')	#set the seperation charicter
		for row in reader:							#read untill there are no rows left
			if (row[6][0] != "-"):					#check if there is no associated document
				docLinks.append([row[1],row[6],row[7],row[8],row[9],row[10]])	#append the documentation links to the multidimensional list
	return docLinks

'''*************************************************************'''
'''************************** Test Call ************************'''
'''*** uncomment the lines below to run this def by its self ***'''
'''*************************************************************'''

# docLinks = []
# docLinks = getDocLinks('testFile.csv')
# counter = 0

# for lines in docLinks:
	# print counter, lines
	# counter = counter + 1
