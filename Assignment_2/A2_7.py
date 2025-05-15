def DisplayPattern(no):
    for i in range(1,no+1,1):
        for j in range(1,no+1,1):
            print(j,end=" ");
        print(" ");

def main():
    no = int(input("Enter number: "))
    DisplayPattern(no)

if(__name__ == "__main__"):
    main()