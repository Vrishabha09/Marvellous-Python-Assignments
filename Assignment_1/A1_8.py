def DisplayStar(no1):
    for i in range(0,no1):
        print("*",end=" ");

def main():
    no1 = int(input("Enter number to print * : "));
    
    DisplayStar(no1);

if(__name__ == "__main__"):
    main()