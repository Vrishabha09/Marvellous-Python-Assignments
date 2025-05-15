
def DisplayPattern(no):
    for i in range(0,no,1):
        for i in range(0,no,1):
            print("*",end=" ")
        print("");
def main():
    no = int(input("Enter number to print pattern :"))

    DisplayPattern(no)
if(__name__ == "__main__"):
    main()