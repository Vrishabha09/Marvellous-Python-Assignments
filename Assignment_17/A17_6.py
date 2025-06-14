import schedule
import time

def Display():
    print("Lunch Time")

def Display2():
    print("Dinner Time")

def main():

    schedule.every().day.at("11:00").do(Display)
    schedule.every().day.at("21:00").do(Display2)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()
