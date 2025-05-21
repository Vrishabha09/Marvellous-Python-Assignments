from functools import reduce

Product = lambda prod, no : prod * no

def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        iList.append(int(input("Enter element : ")))

    print("Input list :",iList)

    Ans = reduce(Product,iList)
    print("Product :",Ans)
    
if(__name__ == "__main__"):
    main()