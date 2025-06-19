import psutil
import schedule
import time

def DisplayProcess():
    Border = "-"*80
    print(Border+"\n")
    print("\tThis script Displays running processes at : "+time.ctime()+"\n")
    print(Border+"\n")

    for process in psutil.process_iter():
        P_info = process.as_dict(attrs=['name','pid','username'])
        print(P_info)
    
    print(Border)


def main():
    schedule.every(1).minutes.do(DisplayProcess)

    while True:
        schedule.run_pending()
        time.sleep(1)
if(__name__ == "__main__"):
    main()