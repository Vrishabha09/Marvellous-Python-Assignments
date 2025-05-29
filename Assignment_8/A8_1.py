import threading

def Even(no):
    iCnt = 1;
    i = 1
    while(iCnt != no):
        if(i % 2 == 0):
            print("Even :",i);
            iCnt = iCnt+1 
        i += 1

def Odd(no):
    iCnt = 1;
    i = 1
    while(iCnt != no):
        if(i % 2 != 0):
            print("Odd :",i);
            iCnt = iCnt+1
        i += 1

def main():
    no = 10
    T_Even = threading.Thread(target=Even,args=(no,))
    T_Odd = threading.Thread(target=Odd,args=(no,))

    T_Even.start()
    T_Odd.start()

    T_Even.join()
    T_Odd.join()

    print("----------End of main---------")

if(__name__ == "__main__"):
    main()