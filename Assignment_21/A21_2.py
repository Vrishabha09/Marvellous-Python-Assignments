import psutil
import schedule
import time
import sys

def DisplayProcess(P_Name):
    Border = "-"*80
    print(Border+"\n")
    print("\tThis script Displays running processes at : "+time.ctime()+"\n")
    print(Border+"\n")

    flag = False;
    pid = 0;
    for process in psutil.process_iter(['name','pid']):

        p = process.info['name'];
        p = p.replace(" ","")
        if p == P_Name:
            flag = True
            pid = process.info['pid']
    
    if flag:
        print("Process is running.")
        print("Ans its pid is :",pid)
    else:
        print("Process is not running")
    
    print(Border)


def main():
    size = len(sys.argv)

    if size == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use this script as : ");
            print("ScriptName.py ProcessName");
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to display status of that process.")
        
        else:
            P_Name = sys.argv[1]

            schedule.every(1).minutes.do(DisplayProcess,P_Name)

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invaid arguements.")
        print("Enter : \n1. ScriptName.py --u(For Usage).\n2. ScriptName.py --h(For Help)")

    
if(__name__ == "__main__"):
    main()