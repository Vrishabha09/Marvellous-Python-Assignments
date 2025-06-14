import schedule
import time
import os

def CFile():
    ctime = time.ctime()
    flag = os.path.exists("Marvellous.txt")

    if flag:
        fd = open("Marvellous.txt","a")
        fd.write("Current time : "+ctime+"\n")
        fd.close()
        print("Time written in Marvellous.txt")
    else:
        fd = open("Marvellous.txt","w")
        Border = "-"*80
        fd.write(Border+"\n")
        fd.write("This is Marvellous automation file.\n")
        fd.write(Border+"\n")
        fd.write("Current time : "+ctime)
        fd.close()
        print("Time written in Marvellous.txt")


def main():

    schedule.every(5).minutes.do(CFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()
