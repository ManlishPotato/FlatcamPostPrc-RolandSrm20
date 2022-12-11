#Benjamin Solar - 11/12-2022
print("Roland nc Post Processor Version 1")

import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
oldFileAdr=askopenfilename()

oldFile=open(oldFileAdr,"r")
allLines=oldFile.readlines()
newFile=open("tempFile","w")

newFile.write("%\n") #Data start
newFile.write("(Roland nc Post Processor Ver1 - By Benjamin Solar)\n\n")

for i in allLines:
    #Remove tool change command T
    if i[0] != 'T':
        newFile.write(i)

newFile.write("M02\n") #Program end
newFile.write("%\n") #Data end

newFile.close()
oldFile.close()

#Replace 
os.replace("tempFile",oldFileAdr)

print("Finished!")
print("Location: " + oldFileAdr)
