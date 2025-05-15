def getMax(iList):
    max = 0
    for data in iList:
        if(max < data):
            max = data
    return max
def main():
    no = int(input("Enter number of elements : "))
    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    result = getMax(iList)

    print("Maximum element of list :",result)

if(__name__ == "__main__"):
    main()