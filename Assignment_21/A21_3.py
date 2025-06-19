import psutil
import os
import time
import schedule
import sys

def CreateLog(folderName):
    Data = ProcessScan()
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    
    timeStamp = time.ctime()
    timeStamp = timeStamp.replace(" ","")
    timeStamp = timeStamp.replace(":","-")
    timeStamp = timeStamp.replace("/","_")

    fileName = os.path.join(folderName,"Marvellous"+timeStamp+".log")
    fobj = open(fileName,"w")

    Border = "-"*80
    fobj.write(Border+"\n")
    fobj.write("\t\tMarvellous Infosystems Process log\n")
    fobj.write("\t\tLog file created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    for d in Data:
        fobj.write(str(d)+"\n\n")

    fobj.write(Border+"\n")
    fobj.close()

def ProcessScan():
    
    listProcess = []
     
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProcess

def main():

    size = len(sys.argv)

    if size == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use this script as : ");
            print("ScriptName.py dirName");
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to create a log file of running process.")
        else:
            DirName = sys.argv[1]
            schedule.every(1).minutes.do(CreateLog,DirName)

            while True:
                schedule.run_pending()
                time.sleep(1)
        
    else:
        print("Invaid arguements.")
        print("Enter : \n1. ScriptName.py --u(For Usage).\n2. ScriptName.py --h(For Help)")

    

if __name__ == "__main__":
    main()