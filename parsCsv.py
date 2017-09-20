import csv		#imports libraries used to read the csv files

def parsCsv(csvLocation): 
	#docLinks is a list of emails found in the csv column 
	docLinks = []
	possibilities = ["email","e-mail","E-mail", "Email"]	#possible ways of having the email column
	index1=0
	index2=0
	with open(csvLocation, 'rU') as csvfile:			#open the CSV file
		reader = csv.reader(csvfile, delimiter = ',')	#set the seperation charicter as a ,
		for row in reader:								#read untill there are no rows left				
			for item in possibilities:
				if item in row:								
			 		index1= possibilities.index(item)	 	#finds the way email column is written
					index2=row.index(possibilities[index1])	#finds the index of the column																					   
															#read untill there are no rows left
				if row[index2]!= possibilities[index1]:		#exclude the title Email from the list
					docLinks.append(row[index2])			#append the email to the list
										
	return docLinks										#return the list to the main script

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