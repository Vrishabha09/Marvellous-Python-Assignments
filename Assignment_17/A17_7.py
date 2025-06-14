import schedule
import time
import os

def BackUp():
    dirpath = "/Users/Studies/Python_AIML/Marvellous_Python_Assignments/"
    dirName = "Assignment_17"
    backup = "back_up"

    destDir = os.path.join(dirpath,dirName)
    print("--------",destDir)

    backup_destDir = os.path.join(dirpath,backup)
    print("--------",backup_destDir)

    flag = os.path.isdir(backup_destDir)

    if flag:
        for folderName, subFolders , files in os.walk(destDir):
            for file in files:
                fd = open(file,"r")
                time_stamp = time.ctime()
                backUp_fName = file+"_back_up_"+time_stamp+".txt"
                finalBackUpdest = os.path.join(backup_destDir,backUp_fName)
                #print(finalBackUpdest)
                fd1 = open(finalBackUpdest,"w")

                for data in fd:
                    fd1.write(data+"\n")
                
                backlog = "back_up_log.log"
                logDest = os.path.join(backup_destDir,backlog)
                fd3 = open(logDest,"a")
                fd3.write(backUp_fName+"\n")

                fd.close()
                fd1.close()
                fd3.close()
                
    else:     
        os.mkdir(backup_destDir)
        fd = open("back_up_log.log","w")
        Border = "-"*80
        fd.write(Border+"\n")
        fd.write("This is Automation that creates backup and this log file stores backup metadata.\n")
        fd.write(Border+"\n")
        fd.close()

def main():
    schedule.every(5).minutes.do(BackUp)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()
