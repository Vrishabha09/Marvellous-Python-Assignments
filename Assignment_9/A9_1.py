import threading
import time

def Display(no):
    print("Displaying for Thread :",threading.current_thread().name)
    for i in range(1,no+1,1):
        print(i)
        time.sleep(1)
    print("-------------------------")

def main():
    T1 = threading.Thread(target=Display,args=(5,),name="T1")
    T2 = threading.Thread(target=Display,args=(5,),name="T2")
    T3 = threading.Thread(target=Display,args=(5,),name="T3")

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    T3.start()
    T3.join()

    print("----------End of main ----------")
if(__name__ == "__main__"):
    main()