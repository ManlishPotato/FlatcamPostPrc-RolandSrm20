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

goToWorkZ=False #Go to work z flag

for i in allLines:
    doWrite=True #Regular write flag

    #Go to Z2mm
    if goToWorkZ==True:
        goToWorkZ=False
        doWrite=False
        newFile.write("G00 Z2.0000\n")
    
    #Remove tool change command T
    if i[0] == 'T':
        doWrite=False
        
    if i == "M6\n":
        doWrite=False

    if i == "M5\n":
        doWrite=False
        newFile.write("M05\n")

    if i == "M0\n":
        doWrite=False
        newFile.write("M00\n")
        goToWorkZ=True #Go to Z2mm after stop

    if doWrite==True:
        newFile.write(i)

newFile.write("M02\n") #Program end
newFile.write("%\n") #Data end

newFile.close()
oldFile.close()

#Replace 
os.replace("tempFile",oldFileAdr)

print("Finished!")
print("Location: " + oldFileAdr)
