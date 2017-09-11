import csv		#imports libraries used to read the csv files

def parsCsv(csvLocation): 
	#docLinks is a list of emails found in the csv column 3
	docLinks = []
	
	with open(csvLocation, 'rU') as csvfile:			#open the CSV file
		reader = csv.reader(csvfile, delimiter = ',')	#set the seperation charicter as a ,
		for row in reader:								#read untill there are no rows left
			if(row[3].lower() != "email"):				#exclude the title Email from the list
				docLinks.append(row[3])					#append the email to the list
	return docLinks										#retrun the list to the main script

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