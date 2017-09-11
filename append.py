#This function reads the list of emails from cvs file and creates a text file with the updated email list
import Tkinter,tkFileDialog,tkMessageBox
from Tkinter import *
def append(cvs_list): #gets list of emails from cvs file
	email_list = []
	directory = tkFileDialog.askdirectory()
	try:
		file = open(directory+'/email_List.txt', 'r') #read existing email file
		file1=file.read()
		email_list = file1.split(';') #create a list from email file
	except:
		open(directory+'/email_List.txt','a').close
	for i in cvs_list:
	  if i not in email_list:  #if the email is not added before
		email_list.append(i)
	with open (directory+'/email_List.txt', 'w') as out:  #update the email list
		out.write(';'.join([str(n) for n in email_list])) #create the updated text file
	tkMessageBox.showinfo("Confirmation", "Your email list is successfully downloaded to "+ directory)