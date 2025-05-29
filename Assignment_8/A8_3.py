import threading

def EvenAdd(iList):
    Sum = 0
    for data in iList:
        if data % 2 == 0:
            Sum += data
    print("Sum of even elements :",Sum)

def OddAdd(iList):
    Sum = 0
    for data in iList:
        if data % 2 != 0:
            Sum += data
    print("Sum of odd elements :",Sum)

def main():
    no = int(input("Enter number of elements in the list : "))
    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data);
    T_Even = threading.Thread(target=EvenAdd,args=(iList,))
    T_Odd = threading.Thread(target=OddAdd,args=(iList,))

    T_Even.start()
    T_Odd.start()

    T_Even.join()
    T_Odd.join()

    print("----------End of main---------")

if(__name__ == "__main__"):
    main()