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

    Duplicate = {}
    if flag:
        for FolderName, Subfolders , Files in os.walk(DirName):
            for file in Files:
                file = os.path.join(FolderName,file)
                Chksum = DisplayCheckSum(file)
                if Chksum in Duplicate:
                    Duplicate[Chksum].append(file)
                else:
                    Duplicate[Chksum] = [file]
    else:
        print("No such directory.")

    return Duplicate

def CreateLog(DirName):
    Dups = TravelDir(DirName)

    Result = list(filter(lambda x : len(x) > 1,Dups.values()))

    timeStamp = time.ctime()
    fName = "Log"+timeStamp+".txt"
    fName = fName.replace(" ","_")
    fName = fName.replace("/","-")

    fd = open(fName,"w")

    Border = "-"*50
    fd.write(Border+"\n")
    fd.write("\tLog file of duplicates present in the directory.\n")
    fd.write(Border+"\n")
    for files in Result:
        for f in files:
            fd.write(f+"\n")

    fd.write(Border+"\n")
    fd.write("\tCreated at :"+time.ctime()+"\n")
    fd.write(Border+"\n")

    fd.close()

def main():

    if len(sys.argv) == 2:
        DirName = sys.argv[1]

        schedule.every(1).minutes.do(CreateLog,DirName)
        
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