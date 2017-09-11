#This function reads the list of emails from cvs file and creates a text file with the updated email list

def append(cvs_list): #gets list of emails from cvs file
	email_list = []
	file = open('test.txt', 'r') #read existing email file
	file1=file.read()
	email_list = file1.split(';') #create a list from email file
	
	for i in cvs_list:
	  if i not in email_list:  #if the email is not added before
		email_list.append(i)
	with open ('test.txt', 'w') as out:  #update the email list
		out.write(';'.join([str(n) for n in email_list])) #create the updated text file