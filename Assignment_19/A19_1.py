import sys
import os

def DisplayFiles(DirName,Extension):
    flag = os.path.isdir(DirName)
    if flag:
       
       for FolderName , SubFolders, Files in os.walk(DirName):
           for file in Files:
               if file.endswith(Extension):
                   print(file)

    

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this file.")
            print("File_Name.py Directory fileExtension")
        elif sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This file dislays files with specified extension.")
    elif len(sys.argv) == 3:
        DirName = sys.argv[1]
        Extension = sys.argv[2]
        DisplayFiles(DirName,Extension)
    else:
        print("Invalid arguements.")
        print("Enter any of 2 commands.\n1. FileName.py --u(Usage).\n2. FileName.py --h(Help)")

if(__name__ == "__main__"):
    main()