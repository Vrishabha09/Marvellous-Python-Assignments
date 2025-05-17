from functools import reduce

ChkPrime = lambda no , i : ((no % i) == 0)

MultiplyX = lambda no : no*2

MaximumX = lambda max, no : no if(no > max) else max

def FilterX(Task,iList):
    FData = list()

    for no in iList:
        if(no <= 1):
            continue
        isPrime = True
    
        for i in range(2,int(no/2)+1):
            if(Task(no,i)):
                isPrime = False

        if(isPrime):
            FData.append(no)
    
    return FData

def MapX(Task,FData):
    MData = list()

    for no in FData:
        MData.append(Task(no))

    return MData

def ReduceX(Task,MData):
    RData = 0
    for no in MData:
        RData = Task(RData,no)

    return RData

def main():
    no1 = int(input("Enter number of elemetns in list : "))

    iList = list()
    for i in range(no1):
        data = int(input("Enter value : "));
        iList.append(data)

    print("Input List :",iList)
    FData = FilterX(ChkPrime,iList)
    print("List after filter (Prime):",FData);

    MData = MapX(MultiplyX,FData)
    print("List after map (*2):",MData)

    RData = ReduceX(MaximumX,MData)
    print("Output of Reduce (Maximum):",RData);

if(__name__ == "__main__"):
    main()