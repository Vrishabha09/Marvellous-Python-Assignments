
def ChkPrime(data):

    if data == 1 or data == 2:
        return True
    else:
        for i in range(2,int(data/2)+1):
            if data % i == 0:
                return False
            
    return True

def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        iList.append(int(input("Enter element : ")))

    print("Input list :",iList)

    iList = list(filter(ChkPrime,iList))
    print("Prime List :",iList)
    
if(__name__ == "__main__"):
    main()