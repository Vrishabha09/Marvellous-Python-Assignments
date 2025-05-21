Double = lambda no : no + no

def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        iList.append(int(input("Enter element : ")))

    print("Input list :",iList)

    iList = list(map(Double,iList))
    print("Doubled List :",iList)
    
if(__name__ == "__main__"):
    main()