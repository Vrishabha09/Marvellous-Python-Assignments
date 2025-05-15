def getFrequency(iList,key):
    freq = 0
    for data in iList:
        if(key == data):
            freq += 1
    return freq

def main():
    no = int(input("Enter number of elements : "))
    if(no <= 0):
        print("Size of List must be atleast 1.")
        return
    
    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    key = int(input("Enter number to count its freq : "))
    result = getFrequency(iList,key)

    print("Frequency of element :",result)

if(__name__ == "__main__"):
    main()