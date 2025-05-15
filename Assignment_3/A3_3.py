def getMax(iList):
    min = iList[0]
    for data in iList:
        if(min > data):
            min = data
    return min

def main():
    no = int(input("Enter number of elements : "))

    if(no <= 0):
        print("Size of List must be atleast 1.")
        return
    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    result = getMax(iList)

    print("Minimum element of list :",result)

if(__name__ == "__main__"):
    main()