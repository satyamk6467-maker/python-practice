# print how many line is present in notes.txt
import os 

try:
    with open("hungry.txt","r")as f:
     listoflines=f.readlines()
    print("output of readlines function",listoflines)
    print("number of lines in file ",len(listoflines ))
except FileNotFoundError:
 print("file does not exist")


    # renaming the file 
# os.rename("report.txt2","satyam.txt")
   