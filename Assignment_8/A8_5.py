import threading

def Display(no):
    print("-------------Display-----------------")
    for i in range(no):
        print(i)
    print("-------------Display-----------------")

def DisplayRev(no):
    print("-------------Display Reverse-----------------")
    for i in range(no,0,-1):
        print(i)
    print("-------------Display Reverse-----------------")


def main():
    no = 50

    T1 = threading.Thread(target=Display,args=(no,))
    T2 = threading.Thread(target=DisplayRev,args=(no,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("------------End of main-------------")
    
if(__name__ == "__main__"):
    main()