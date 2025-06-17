import sys
import os
import hashlib
import schedule
import time

def DisplayCheckSum(fName,BlockSize = 1024):
    fd = open(fName,"rb")                        

    hobj = hashlib.md5()

    buffer = fd.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fd.read(BlockSize)

    fd.close()

    return hobj.hexdigest()

def TravelDir(DirName):
    flag = os.path.isdir(DirName)

    if flag:
        for FolderName, Subfolders , Files in os.walk(DirName):
            for file in Files:
                print("File :",file,end=" ")
                file = os.path.join(FolderName,file)
                Chksum = DisplayCheckSum(file)
                print("Check sum :",Chksum)
    else:
        print("No such directory.")

def main():

    if len(sys.argv) == 2:
        DirName = sys.argv[1]

        schedule.every(1).minutes.do(TravelDir,DirName)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == '--u' or sys.argv[1] == '--U':
                print("Usage of this file.")
                print("File_Name.py Directory fileExtension")
            elif sys.argv[1] == '--h' or sys.argv[1] == '--H':
                print("This file dislays files with specified extension.")
        else:
            print("Invalid arguements.")
            print("Enter any of 2 commands.\n1. FileName.py --u(Usage).\n2. FileName.py --h(Help)")

if(__name__ == "__main__"):
    main()