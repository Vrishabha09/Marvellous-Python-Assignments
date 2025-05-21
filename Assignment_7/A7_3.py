ChkEven = lambda no : no%2 == 0

def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        iList.append(int(input("Enter element : ")))

    print("Input list :",iList)

    iList = list(filter(ChkEven,iList))
    print("Even List :",iList)
    
if(__name__ == "__main__"):
    main()