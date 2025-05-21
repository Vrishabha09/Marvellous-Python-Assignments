def Max(iList):
    Max = -1
    for data in iList:
        if Max < data:
            Max = data
    print("Maximum :",Max)

def main():
    iList = list()
    
    print("Enter 5 number to find out maximum.")
    for i in range(5):
        data = int(input("Enter element : "))
        iList.append(data)
    
    Max(iList)

if(__name__ == "__main__"):
    main()