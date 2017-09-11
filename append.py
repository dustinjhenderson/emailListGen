
def append(cvs_list):
	#cvs_list=["ezgi@gmail.com", "dustin@gmail.com"];
	email_list = []
	file = open('test.txt', 'r') #read existing email file
	file1=file.read()
	print "email list before: "
	print file1
	email_list = file1.split(';') #create email list file
	
	for i in cvs_list:
	  if i not in email_list:
		email_list.append(i)
	print "email_list: "
	print email_list
	with open ('test.txt', 'w') as out:
		out.write(';'.join([str(n) for n in email_list]))
  






