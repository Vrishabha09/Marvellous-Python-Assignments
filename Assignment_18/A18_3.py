import os
import shutil

def CopyFile(fName):
    flag = os.path.isfile(fName)
    if flag:
       shutil.copyfile(fName,"Demo.txt")
    else:
        print("File not present.")

def main():
    fName = input("Enter file name : ")
    CopyFile(fName)

if(__name__ == "__main__"):
    main()