from functools import reduce

ChkEven = lambda no : ((no % 2) == 0)

SquareX = lambda no : no**2

AdditionX = lambda sum, no : sum + no

def main():
    no1 = int(input("Enter number of elemetns in list : "))

    iList = list()
    for i in range(no1):
        data = int(input("Enter value : "));
        iList.append(data)

    print("Input List :",iList)
    FData = list(filter(ChkEven,iList))
    print("List after filter :",FData);

    MData = list(map(SquareX,FData))
    print("List after map :",MData)

    RData = reduce(AdditionX,MData)
    print("Output of Reduce :",RData);

if(__name__ == "__main__"):
    main()