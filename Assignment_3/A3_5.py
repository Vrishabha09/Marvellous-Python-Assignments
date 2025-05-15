from MarvellousNum import ChkPrime

def ListPrime(iList):
    sum = 0
    for data in iList:
        if(ChkPrime(data)):
            sum += data
    return sum

def main():
    no = int(input("Enter number of elements : "))

    if(no <= 0):
        print("Size of List must be atleast 1.")
        return
    
    iList = list()

    for i in range(no):
        data = int(input("Enter elemnet : "))
        iList.append(data)

    result = ListPrime(iList)
    print("Sum of all prime numbers :",result);

if(__name__ == "__main__"):
    main()