#Benjamin Solar - 11/12-2022
print("Roland nc Post Processor Version 1")

import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
oldFileAdr=askopenfilename()

oldFile=open(oldFileAdr,"r")
allLines=oldFile.readlines()
newFile=open("TempFile.nc","w")

newFile.write("%\n") #Data start
newFile.write("(Roland nc Post Processor Ver1 - By Benjamin Solar)\n\n")

skipNext=0

for i in allLines:
    doWrite=True #Regular write flag

    #Replace next line
    if skipNext > 0:
        skipNext-=1
        doWrite=False
    else:
        #Remove tool change command T
        if i[0] == 'T':
            doWrite=False

        #Remove tool change command M06
        if i == "M6\n":
            doWrite=False

        if i == "M5\n":
            doWrite=False
            newFile.write("M05\n")

        if i == "M0\n":
            doWrite=False
            newFile.write("M00\n")

    if doWrite==True:
        newFile.write(i)

newFile.write("G00 Z15.0000\n") #Go to Z15mm
newFile.write("G00 X0.0000 Y0.0000\n") #Go to home
newFile.write("M02\n") #Program end
newFile.write("%\n") #Data end

newFile.close()
oldFile.close()

#Replace 
os.replace("TempFile.nc",oldFileAdr)

print("Finished!")
print("Location: " + oldFileAdr)
