from functools import reduce

RangeX = lambda no : True if 70 <= no <= 90 else False

IncreaseX = lambda no : no+10

Multiply = lambda mult, no : mult * no

def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        data = int(input(f"Enter element {i+1}: "))
        iList.append(data)

    print("Original list :",iList)

    FData = list(filter(RangeX,iList))
    print("Filtered list :",FData)

    MData = list(map(IncreaseX,FData))
    print("Mapped data :",MData)

    RData = reduce(Multiply,MData)
    print("Reduced Data :",RData)
    
if(__name__ == "__main__"):
    main()