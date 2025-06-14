import schedule
import time
import datetime

def Display():
    date = datetime.datetime.now()
    print(date)

def main():

    schedule.every(1).minutes.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()