import sys
import os
import shutil

def CpyDirs(DirName1,DirName2):
    flag = os.path.isdir(DirName1)
    
    if flag:
        flag2 = os.path.isdir(DirName2)
        if flag2:
            print(DirName2,"already exists.")
            exit()

        os.mkdir(DirName2)
        DirName1 = os.path.abspath(DirName1)
        DirName2 = os.path.abspath(DirName2)
        for FolderName , SubFolders, Files in os.walk(DirName1):
            for file in Files:
                currPath = os.path.join(FolderName,file)
                shutil.copy2(currPath,DirName2)
                

                               

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this file.")
            print("File_Name.py Directory fileExtension")
        elif sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This file copies files from 1 directory to other files.")
    elif len(sys.argv) == 3:
        DirName1 = sys.argv[1]
        DirName2 = sys.argv[2]
        CpyDirs(DirName1,DirName2)
    else:
        print("Invalid arguements.")
        print("Enter any of 2 commands.\n1. FileName.py --u(Usage).\n2. FileName.py --h(Help)")

if(__name__ == "__main__"):
    main()