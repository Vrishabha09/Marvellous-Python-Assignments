import threading

def EvenFactor(no):
    Sum = 0
    for i in range(1,int(no/2)+1):
        if no % i == 0:
            if i % 2 == 0:
                Sum += i
    print("Sum of even factors :",Sum)

def OddFactor(no):
    Sum = 0
    for i in range(1,int(no/2)+1):
        if no % i == 0:
            if i % 2 != 0:
                Sum += i
    print("Sum of odd factors :",Sum)

def main():
    no = int(input("Enter number to print its sum Even and Odd Factor : "))
    T_Even = threading.Thread(target=EvenFactor,args=(no,))
    T_Odd = threading.Thread(target=OddFactor,args=(no,))

    T_Even.start()
    T_Odd.start()

    T_Even.join()
    T_Odd.join()

    print("----------End of main---------")

if(__name__ == "__main__"):
    main()