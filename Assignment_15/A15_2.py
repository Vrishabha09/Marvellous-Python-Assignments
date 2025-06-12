#-----------------File 1---------------

import os

def DisplayFile(fName):
    Ans = os.path.exists(fName)
    if Ans:
        fobj = open(fName,"r")
        data = fobj.read()

        print("Data from file : ")
        print(data)
    else:
        print("File not Present")

def main():
    fName = input("Enter file name : ")
    DisplayFile(fName)

if(__name__ == "__main__"):
    main()