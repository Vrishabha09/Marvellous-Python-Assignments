from functools import reduce

def RangeX(no): 
    if(70 <= no <= 90):
        return True
    else:
        return False

def IncreaseX(no):
    return no+10

def ProductX(prod,no):
    return prod*no

def main():
    no1 = int(input("Enter number of elemetns in list : "))

    iList = list()
    for i in range(no1):
        data = int(input("Enter value : "));
        iList.append(data)

    print("Input List :",iList)
    FData = list(filter(RangeX,iList))
    print("List after filter :",FData);

    MData = list(map(IncreaseX,FData))
    print("List after map :",MData)

    RData = reduce(ProductX,MData)
    print("Output of Reduce :",RData);

if(__name__ == "__main__"):
    main()