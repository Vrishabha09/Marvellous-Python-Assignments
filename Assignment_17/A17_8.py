import schedule
import time

def ChkEmail():
    print("Checking email........")

def main():

    schedule.every(10).seconds.do(ChkEmail)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()
