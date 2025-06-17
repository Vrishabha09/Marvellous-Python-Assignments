import sys
import os

def renameFiles(DirName,Extension1,Extension2):
    flag = os.path.isdir(DirName)
    if flag:
       
       for FolderName , SubFolders, Files in os.walk(DirName):
           for file in Files:
               if file.endswith(Extension1):
                   old = os.path.join(FolderName,file)
                   name = file.split(".")
                   newName = name[0]+Extension2
                   newPath = os.path.join(FolderName,newName)
                   os.rename(old,newPath)  

       print("Successfully changed extension of files.")                 

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this file.")
            print("File_Name.py Directory fileExtension")
        elif sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This file compares two files.")
    elif len(sys.argv) == 4:
        DirName = sys.argv[1]
        Extension1 = sys.argv[2]
        Extension2 = sys.argv[3]
        renameFiles(DirName,Extension1,Extension2)
    else:
        print("Invalid arguements.")
        print("Enter any of 2 commands.\n1. FileName.py --u(Usage).\n2. FileName.py --h(Help)")

if(__name__ == "__main__"):
    main()