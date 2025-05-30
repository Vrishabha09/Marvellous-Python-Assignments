import multiprocessing
import os

def DisplayFactorial(no):
    data = 1
    for i in range(1,no+1):
        data = data*i
    return data  

def main():
    no = int(input("Enter number of elements : "))

    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    print("Original list :",iList)
    P1 = multiprocessing.Pool()
    result = P1.map(DisplayFactorial,iList)

    print("Result factorial list of all elements :",result)
    
    P1.close()
    P1.join()

    print("----------End of main ----------")
if(__name__ == "__main__"):
    main()