import os
import shutil

def CopyFile(fName,srcFile):
    Ans = os.path.exists(fName)
    if Ans:
        Border = "-"*80
        print(Border)
        print("File "+fName+" already present in this directory.")
        print("Copying data will result in overwritting of over exsiting data.")
        print(Border)
    else:
        shutil.copyfile(srcFile,fName)
        print("Data from",srcFile,"successfully copied into new file",fName)

def main():
    fName = input("Enter file name you want to create : ")
    srcFile = input("Enter name of file from which you want to create data : ")
    CopyFile(fName,srcFile)

if(__name__ == "__main__"):
    main()