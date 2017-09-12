#main script
#This script pulls all the pieces together
#Call each part here when they are all completed

import csv		#imports libraries used to read the csv files
#import string
from append import append
from parsCsv import parsCsv
import Tkinter,tkFileDialog,tkMessageBox  #Used Tkinter library for creating the GUI
from tkFileDialog import askopenfilename
from Tkinter import *


root = Tkinter.Tk()
T = Text(root, height=6, width=100)
T.pack()
T.insert(END, "Welcome to email generator!\n\n\n\nPlease upload your .cvs file and select a directory to download your updated email address list.\n")
T.tag_add("color1", "1.0", "10.0")
T.tag_config("color1",background="black",foreground="green")

fileName = tkFileDialog.askopenfilename()
if fileName != "":
	tkMessageBox.showinfo("Confirmation", "Your file is uploaded successfully!")
	csvLocation = fileName
	listFromCsv = parsCsv(csvLocation)
	append(listFromCsv)
if fileName == "":
	 root.destroy()

