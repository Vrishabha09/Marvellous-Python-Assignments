import time
import multiprocessing
import threading

def DisplaySum():
    Sum = 0
    for i in range(10000001):
        Sum += i
    print("Sum of 1 - 10 million :",Sum)

def main():
    
    start = time.time()
    print("--------For normal function--------")
    DisplaySum()
    end = time.time()
    print("Time taken :",f"{(end-start):3f}")

    start = time.time()
    print("--------For thread function--------")
    T1 = threading.Thread(target=DisplaySum)

    T1.start()
    T1.join()
    end = time.time()
    print("Time taken :",f"{(end-start):3f}")

    start = time.time()
    print("--------For multiprocessing function--------")
    P1 = multiprocessing.Process(target=DisplaySum)

    P1.start()
    P1.join()
    end = time.time()
    print("Time taken :",f"{(end-start):3f}")


if(__name__ == "__main__"):
    main()