def ListSum(iList):
    sum = 0
    for data in iList:
        sum += data

    return sum
def main():
    no = int(input("Enter number of elements : "))
    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    result = ListSum(iList)

    print("Addition of all elements of list :",result)

if(__name__ == "__main__"):
    main()